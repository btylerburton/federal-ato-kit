"""Synthetic negative fixtures verify that integrity checks cannot create false assurance."""

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from heartbeat import checkpoint
from verify import MARKER, claim_checks, confined, digest, package_checks, read_json

NOW = datetime(2026, 11, 6, 18, tzinfo=timezone.utc)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ato-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "proof.txt").write_text("synthetic successful observation\n")
        self.item = {
            "id": "E1", "kind": "offline-test", "environment": "fixture",
            "source_revision": "fixture-v1", "observed_at": "2026-11-06T17:00:00Z",
            "expires_at": "2026-11-07T17:00:00Z", "artifact": "proof.txt",
            "sha256": digest((self.root / "proof.txt").read_bytes()),
            "method": "synthetic unit fixture", "observation": "fixture passed", "result": "PASS",
        }
        self.claim = {
            "id": "C1", "statement": "Synthetic fixture result", "controls": ["SA-11"],
            "environment": "fixture", "source_revision": "fixture-v1",
            "required_kind": "offline-test", "evidence_ids": ["E1"],
        }

    def status(self):
        return claim_checks({"schema_version": 1, "claims": [self.claim],
                             "evidence": [self.item]}, self.root, NOW)[0]["status"]

    def test_matching_evidence_then_tampering(self):
        self.assertEqual(self.status(), "PASS")
        (self.root / "proof.txt").write_text("changed")
        self.assertEqual(self.status(), "FAIL")

    def test_offline_cannot_prove_live(self):
        self.claim["required_kind"] = "live-test"
        self.assertEqual(self.status(), "BLOCKED")

    def test_revision_and_environment_must_match(self):
        for field in ["source_revision", "environment"]:
            with self.subTest(field=field):
                original = self.claim[field]
                self.claim[field] = "other"
                self.assertEqual(self.status(), "BLOCKED")
                self.claim[field] = original

    def test_expired_future_and_naive_timestamps(self):
        self.item["expires_at"] = "2026-11-06T17:30:00Z"
        self.assertEqual(self.status(), "BLOCKED")
        self.item["observed_at"] = "2026-11-08T17:00:00Z"
        self.assertEqual(self.status(), "FAIL")
        self.item["observed_at"] = "2026-11-06T17:00:00"
        with self.assertRaisesRegex(ValueError, "timezone"):
            self.status()

    def test_missing_and_failed_evidence(self):
        self.item["result"] = "FAIL"
        self.assertEqual(self.status(), "FAIL")
        self.claim["evidence_ids"] = ["missing"]
        self.assertEqual(self.status(), "BLOCKED")
        self.claim["evidence_ids"] = []
        self.assertEqual(self.status(), "NOT_ASSESSED")

    def test_escape_and_symlink_rejected(self):
        with self.assertRaisesRegex(ValueError, "escapes"):
            confined(self.root, "../outside")
        (self.root / "escape").symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "escapes"):
            confined(self.root, "escape/outside")

    def test_duplicate_json_keys_rejected(self):
        path = self.root / "invalid.json"
        path.write_text('{"result":"FAIL","result":"PASS"}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            read_json(path)

    def test_duplicate_evidence_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate evidence ID"):
            claim_checks({"schema_version": 1, "claims": [self.claim],
                          "evidence": [self.item, self.item]}, self.root, NOW)

    def test_package_hash_and_inventory(self):
        folder = self.root / "control-statements/ac"
        folder.mkdir(parents=True)
        control = folder / "ac-2.md"
        control.write_text("---\n---\n" + MARKER + "original\n")
        index = {"controls": [{"control_id": "ac-2", "path": "control-statements/ac/ac-2.md",
                               "source_sha256": digest(b"original"), "source_status_selections": []}]}
        (self.root / "migration-index.json").write_text(json.dumps(index))
        checks = package_checks(self.root)
        self.assertEqual(checks[0]["status"], "PASS")
        self.assertEqual(checks[1]["status"], "BLOCKED")
        control.write_text(MARKER + "modified\n")
        self.assertEqual(package_checks(self.root)[0]["status"], "FAIL")
        index["controls"] = []
        (self.root / "migration-index.json").write_text(json.dumps(index))
        with self.assertRaisesRegex(ValueError, "Nonempty"):
            package_checks(self.root)

    def test_heartbeat_stops_and_appends_honestly(self):
        state, log = self.root / "state.json", self.root / "heartbeats.jsonl"
        state.write_text(json.dumps({"iteration": 1, "status": "in_progress"}))
        self.assertFalse(checkpoint(state, log))
        state.write_text(json.dumps({"iteration": 1, "status": "complete"}))
        self.assertTrue(checkpoint(state, log))
        entries = [json.loads(line) for line in log.read_text().splitlines()]
        self.assertEqual(len(entries), 2)
        self.assertIsNone(entries[0]["last_agent_reflection"])
        self.assertEqual(entries[1]["status"], "complete")


if __name__ == "__main__":
    unittest.main()

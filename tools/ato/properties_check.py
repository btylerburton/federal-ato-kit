"""Portable dependency-backed tests: invoke with an isolated environment's pytest."""

from hypothesis import given, settings, strategies as st

from verify import digest


@settings(max_examples=100, database=None)
@given(st.binary(max_size=4096))
def test_artifact_mutation_changes_digest(data):
    assert digest(data) != digest(data + b"\x00")


@settings(max_examples=100, database=None)
@given(st.binary(max_size=4096))
def test_digest_has_stable_sha256_encoding(data):
    result = digest(data)
    assert len(result) == 64
    assert bytes.fromhex(result).hex() == result
    assert digest(bytes(data)) == result

#!/usr/bin/env python3
"""Emit project-supplied progress checkpoints; this timer does not invoke an AI agent."""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def checkpoint(state_path, log_path):
    state = json.loads(state_path.read_text())
    status = state["status"]
    if status not in {"in_progress", "blocked", "complete", "cancelled"}:
        raise ValueError("Invalid iteration status")
    entry = {
        "timestamp": utc_now(),
        "actor": "ato-heartbeat-timer",
        "iteration": state["iteration"],
        "status": status,
        "last_agent_reflection": state.get("last_agent_reflection"),
        "message": "Agent reflection due; timer has not performed a review.",
    }
    if status in {"complete", "cancelled"}:
        entry["message"] = "Iteration stopped; heartbeat exiting."
    with log_path.open("a") as stream:
        stream.write(json.dumps(entry) + "\n")
    print(json.dumps(entry), flush=True)
    return status in {"complete", "cancelled"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--interval", type=int, default=600)
    args = parser.parse_args()
    if args.interval < 1:
        parser.error("interval must be positive")
    # Read state each second to stop promptly, but emit due checkpoints every interval.
    due = 0.0
    while True:
        state = json.loads(args.state.read_text())
        if time.monotonic() >= due or state["status"] in {"complete", "cancelled"}:
            if checkpoint(args.state, args.log):
                return
            due = time.monotonic() + args.interval
        time.sleep(1)


if __name__ == "__main__":
    main()

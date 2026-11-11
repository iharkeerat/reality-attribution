#!/usr/bin/env python3
"""Verify the exact GridWorld *saved enumeration artifact* (not simulator replay).

Uses only Python's standard library. A passing run shows that the archived
CSV has the registered SHA-256 and reaggregates to the declared finite-domain
comparison counts; it does not regenerate simulator trajectories.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "evidence" / "gridworld" / "identifiability_enumeration.csv"
EXPECTED_SHA256 = "d7346f6a307e4b711738ac45cc81df517490005edae39595a50d3e4e84eb3f48"
EXPECTED_ROWS = 16_368
EXPECTED_COMPARISONS = 392_832
PER_CELL = 32_736
ACTIONS_PER_CELL = 1_364
PAIR_F2_F4 = ("i_o_f2", "i_o_f4")
PAIR_M_F2 = ("i_o_f2", "m_lag")
PAIR_M_F4 = ("i_o_f4", "m_lag")
CONTRACT_FIELDS = {
    "none": set(),
    "wall_contact": {"wall_contact"},
    "landmark_identity": {"landmark_identity"},
    "wall_contact+landmark_identity": {"wall_contact", "landmark_identity"},
}
EXPECTED_UNRESOLVED = {
    "none": {PAIR_M_F2: 114, PAIR_M_F4: 32_736, PAIR_F2_F4: 114},
    "wall_contact": {PAIR_M_F2: 114, PAIR_M_F4: 15_900, PAIR_F2_F4: 114},
    "landmark_identity": {PAIR_M_F2: 92, PAIR_M_F4: 23_263, PAIR_F2_F4: 114},
    "wall_contact+landmark_identity": {PAIR_M_F2: 92, PAIR_M_F4: 11_444, PAIR_F2_F4: 114},
}
REQUIRED_COLUMNS = {
    "policy_id", "actions", "horizon", "hypothesis_a", "hypothesis_b",
    "protected_channels", "channel_set_id", "exact_coverage_count",
    "identifiable_state_count", "unresolved_state_count",
    "identifiable_any_state", "identifiable_all_states",
}


class EvidenceError(ValueError):
    """A saved evidence artifact failed the registered integrity checks."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise EvidenceError(message)


def verify(path: Path = DATA_PATH) -> dict:
    """Verify the byte hash, row schema, finite design and all 12 aggregates."""
    content = path.read_bytes()
    actual_hash = hashlib.sha256(content).hexdigest()
    _require(
        actual_hash == EXPECTED_SHA256,
        f"SHA-256 mismatch: found {actual_hash}; expected {EXPECTED_SHA256}. "
        "Check byte integrity and CRLF line endings.",
    )
    try:
        source = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise EvidenceError("Dataset is not UTF-8") from exc

    reader = csv.DictReader(io.StringIO(source, newline=""))
    _require(reader.fieldnames is not None, "Missing CSV header")
    _require(set(reader.fieldnames) == REQUIRED_COLUMNS, "Unexpected CSV columns")

    unresolved = defaultdict(int)
    total = defaultdict(int)
    counts = defaultdict(int)
    actions_seen = defaultdict(set)
    horizon_counts = defaultdict(int)
    row_count = 0

    for row in reader:
        row_count += 1
        pair = tuple(sorted((row["hypothesis_a"], row["hypothesis_b"])))
        contract = row["channel_set_id"]
        key = (contract, pair)

        _require(contract in EXPECTED_UNRESOLVED, f"Row {row_count}: unknown contract")
        _require(pair in EXPECTED_UNRESOLVED[contract], f"Row {row_count}: unknown mechanism pair")

        try:
            actions = json.loads(row["actions"])
            fields = json.loads(row["protected_channels"])
            horizon = int(row["horizon"])
            coverage = int(row["exact_coverage_count"])
            identified = int(row["identifiable_state_count"])
            unresolved_count = int(row["unresolved_state_count"])
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            raise EvidenceError(f"Row {row_count}: invalid value") from exc

        _require(
            isinstance(actions, list)
            and 1 <= len(actions) <= 5
            and all(isinstance(a, int) and a in (0, 1, 2, 3) for a in actions),
            f"Row {row_count}: invalid action sequence",
        )
        _require(horizon == len(actions), f"Row {row_count}: horizon mismatch")
        _require(isinstance(fields, list) and set(fields) == CONTRACT_FIELDS[contract],
                 f"Row {row_count}: protected field mismatch")
        _require(coverage == 24, f"Row {row_count}: unexpected state coverage")
        _require(0 <= identified <= coverage and identified + unresolved_count == coverage,
                 f"Row {row_count}: inconsistent state counts")
        _require(row["identifiable_any_state"] in ("True", "False")
                 and (row["identifiable_any_state"] == "True") == (identified > 0),
                 f"Row {row_count}: inconsistent any-state flag")
        _require(row["identifiable_all_states"] in ("True", "False")
                 and (row["identifiable_all_states"] == "True") == (identified == coverage),
                 f"Row {row_count}: inconsistent all-states flag")

        action_key = tuple(actions)
        _require(action_key not in actions_seen[key],
                 f"Row {row_count}: duplicate action sequence within cell")
        actions_seen[key].add(action_key)
        counts[key] += 1
        horizon_counts[key, horizon] += 1
        total[key] += coverage
        unresolved[key] += unresolved_count

    _require(row_count == EXPECTED_ROWS, f"Expected {EXPECTED_ROWS} rows; found {row_count}")
    _require(len(counts) == 12, f"Expected 12 mechanism/contract cells; found {len(counts)}")

    for contract, pair_counts in EXPECTED_UNRESOLVED.items():
        for pair, expected in pair_counts.items():
            key = (contract, pair)
            _require(counts[key] == ACTIONS_PER_CELL, f"{key}: unexpected policy count")
            _require(total[key] == PER_CELL, f"{key}: unexpected comparison count")
            _require(unresolved[key] == expected,
                     f"{key}: unresolved = {unresolved[key]} (expected {expected})")
            for horizon in range(1, 6):
                _require(horizon_counts[key, horizon] == 4 ** horizon,
                         f"{key}: wrong number of horizon-{horizon} actions")

    full_comparisons = sum(total.values())
    _require(full_comparisons == EXPECTED_COMPARISONS, "Wrong total comparison coverage")
    return {
        "sha256": actual_hash,
        "rows": row_count,
        "comparisons": full_comparisons,
        "counts": dict(unresolved),
    }


def main() -> int:
    try:
        report = verify()
    except (OSError, EvidenceError) as exc:
        print(f"FAILED: {exc}")
        return 1

    print(f"PASS — SHA-256: {report['sha256']}")
    print(f"Rows: {report['rows']:,}; exact comparisons: {report['comparisons']:,}")
    print("Contract                       M/I-F2    M/I-F4    I-F2/I-F4")
    for contract in CONTRACT_FIELDS:
        vals = [report["counts"][(contract, pair)] for pair in
                (PAIR_M_F2, PAIR_M_F4, PAIR_F2_F4)]
        print(f"{contract:30s} {vals[0]:>6,d}    {vals[1]:>6,d}       {vals[2]:>6,d}")
    print("Scope: saved-CSV verification only; not a fresh simulator enumeration.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

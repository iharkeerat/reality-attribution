"""Basic regression checks for the saved GridWorld evidence verifier."""
import tempfile
import unittest
from pathlib import Path

from tools.verify_gridworld_enumeration import (
    DATA_PATH, EvidenceError, EXPECTED_COMPARISONS, EXPECTED_ROWS,
    EXPECTED_SHA256, PAIR_M_F4, verify,
)


class GridWorldEvidenceTests(unittest.TestCase):
    def test_reference_artifact(self):
        summary = verify(DATA_PATH)
        self.assertEqual(summary["sha256"], EXPECTED_SHA256)
        self.assertEqual(summary["rows"], EXPECTED_ROWS)
        self.assertEqual(summary["comparisons"], EXPECTED_COMPARISONS)
        self.assertEqual(summary["counts"][("wall_contact+landmark_identity", PAIR_M_F4)], 11444)

    def test_tampered_artifact_is_rejected(self):
        source = DATA_PATH.read_bytes()
        with tempfile.TemporaryDirectory() as td:
            modified = Path(td) / "mutated.csv"
            modified.write_bytes(source.replace(b"open_loop_0", b"open_loop_X", 1))
            with self.assertRaises(EvidenceError):
                verify(modified)


if __name__ == "__main__":
    unittest.main()

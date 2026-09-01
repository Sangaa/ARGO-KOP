import re
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class Core003Arc011AuthorityBoundaryTest(unittest.TestCase):
    def test_constitution_governs_canonical_architecture_without_dependency_promotion(self):
        core003 = (ROOT / "Core" / "CORE-003_CONSTITUTION.md").read_text(encoding="utf-8")
        arc011 = (ROOT / "Architecture" / "ARC-011_CANONICAL_ARCHITECTURE_MODEL.md").read_text(encoding="utf-8")
        rep014 = (ROOT / "Repository" / "REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md").read_text(encoding="utf-8")
        core_status = (ROOT / "Core" / "_FOLDER_STATUS.md").read_text(encoding="utf-8")

        self.assertIn("Highest governing rules", core003)
        self.assertRegex(core003, re.compile(r"all repository components shall comply", re.IGNORECASE))
        self.assertIn("subordinate to the Constitution", arc011)
        self.assertIn("Constitution / applicable Governance authority", arc011)
        self.assertIn("Canonical Architecture Model", arc011)

        self.assertEqual(rep014.count("| REL-068 | CORE-003 | ARC-011 | GOVERNS |"), 1)
        self.assertEqual(rep014.count("| REL-069 | ARC-011 | CORE-003 | REFERENCES |"), 1)

        forbidden = (
            "| CORE-003 | ARC-011 | DEPENDS_ON |",
            "| ARC-011 | CORE-003 | DEPENDS_ON |",
            "| ARC-011 | CORE-003 | GOVERNS |",
            "| CORE-003 | ARC-011 | IMPLEMENTS |",
            "| CORE-003 | ARC-011 | CONSUMES |",
        )
        for marker in forbidden:
            self.assertNotIn(marker, rep014)

        self.assertIn("CROSS-LAYER VALIDATION OPEN", core_status)
        self.assertIn("Folder Certification\n\n⏳ Pending", core_status)


if __name__ == "__main__":
    unittest.main()

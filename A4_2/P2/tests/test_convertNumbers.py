import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPO_ROOT / "A4_2" / "P2" / "source" / "convertNumbers.py"


def test_converts_numbers(tmp_path: Path):
    sample_file = tmp_path / "ints.txt"
    sample_file.write_text("10\n255\n-10\nbad\n", encoding="utf-8")

    run = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(sample_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert "ITEM\tDEC\tBIN\tHEX" in run.stdout
    assert "\t10\t1010\tA" in run.stdout
    assert "\t255\t11111111\tFF" in run.stdout
    assert "\t-10\t-1010\t-A" in run.stdout

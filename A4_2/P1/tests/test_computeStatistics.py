import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPO_ROOT / "A4_2" / "P1" / "source" / "computeStatistics.py"


def test_runs_and_prints_statistics(tmp_path: Path):
    sample_file = tmp_path / "numbers.txt"
    sample_file.write_text("1\n2\n3\n3\nx\n", encoding="utf-8")

    run = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(sample_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert run.returncode in (0, 1)
    assert "Mean:" in run.stdout
    assert "Median:" in run.stdout
    assert "Mode:" in run.stdout

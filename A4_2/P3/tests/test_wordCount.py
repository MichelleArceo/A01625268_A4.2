import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPO_ROOT / "A4_2" / "P3" / "source" / "wordCount.py"


def test_counts_words(tmp_path: Path):
    sample_file = tmp_path / "words.txt"
    sample_file.write_text("Hola hola, mundo!\nMundo mundo.\n", encoding="utf-8")

    run = subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(sample_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert "mundo\t3" in run.stdout
    assert "hola\t2" in run.stdout

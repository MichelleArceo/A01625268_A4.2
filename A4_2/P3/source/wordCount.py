#!/usr/bin/env python3
"""
wordCount.py

Reads a text file with words separated by spaces/newlines. Identifies distinct
words and their frequencies using basic algorithms (no Counter).

Outputs results to console and to WordCountResults.txt, and reports elapsed time.
"""

from __future__ import annotations

import sys
import time
from typing import Dict, List, Tuple


OUTPUT_FILENAME = "WordCountResults.txt"
PUNCTUATION = ".,;:!?\"'()[]{}<>"


def normalize_word(token: str) -> str:
    """Lowercase and strip punctuation from both ends."""
    word = token.strip().lower()

    while word and word[0] in PUNCTUATION:
        word = word[1:]
    while word and word[-1] in PUNCTUATION:
        word = word[:-1]

    return word


def read_words(file_path: str) -> Tuple[List[str], List[str]]:
    words: List[str] = []
    issues: List[str] = []

    try:
        with open(file_path, "r", encoding="utf-8") as input_file:
            for raw_line in input_file:
                line = raw_line.strip()
                if not line:
                    continue
                for token in line.split():
                    normalized = normalize_word(token)
                    if normalized:
                        words.append(normalized)
    except FileNotFoundError:
        issues.append(f"File not found: {file_path}")
    except OSError as exc:
        issues.append(f"Could not read file '{file_path}': {exc}")

    return words, issues


def count_frequencies(words: List[str]) -> Tuple[Dict[str, int], Dict[str, int]]:
    """Return (frequency_map, first_seen_index) for stable sorting."""
    frequency_map: Dict[str, int] = {}
    first_seen_index: Dict[str, int] = {}

    for index, word in enumerate(words):
        if word not in frequency_map:
            frequency_map[word] = 1
            first_seen_index[word] = index
        else:
            frequency_map[word] += 1

    return frequency_map, first_seen_index


def sort_words_by_frequency(
    frequency_map: Dict[str, int],
    first_seen_index: Dict[str, int],
) -> List[str]:
    """Sort by frequency desc, then first appearance asc."""
    word_list = list(frequency_map.keys())
    word_list.sort(key=lambda w: (-frequency_map[w], first_seen_index[w]))
    return word_list


def write_output_file(lines: List[str]) -> None:
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        for line in lines:
            output_file.write(line + "\n")


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return 2

    input_path = argv[1]
    start_time = time.perf_counter()

    words, issues = read_words(input_path)
    for msg in issues:
        print(f"ERROR: {msg}")

    output_lines: List[str] = []
    base_name = input_path.split("/")[-1]
    output_lines.append(f"Row Labels\tCount of {base_name}")

    if not words:
        output_lines.append("(no words found)\t0")
    else:
        frequency_map, first_seen = count_frequencies(words)
        ordered_words = sort_words_by_frequency(frequency_map, first_seen)
        for word in ordered_words:
            output_lines.append(f"{word}\t{frequency_map[word]}")

    elapsed = time.perf_counter() - start_time
    output_lines.append(f"Time Elapsed (s):\t{elapsed:.6f}")

    for line in output_lines:
        print(line)

    write_output_file(output_lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""Convert numbers to binary and hexadecimal.

Reads a text file with integer values (one per line). Converts each integer to
binary and hexadecimal using basic algorithms (no bin/hex/format).

Outputs results to console and to ConvertionResults.txt, while logging invalid
lines and continuing execution. Reports elapsed execution time at the end.

Note:
    The filename must remain 'convertNumbers.py' as required by Activity A4.2.
"""
# pylint: disable=invalid-name

from __future__ import annotations

import sys
import time
from typing import List, Tuple

OUTPUT_FILENAME = "ConvertionResults.txt"
HEX_SYMBOLS = "0123456789ABCDEF"


def read_integer_values(file_path: str) -> Tuple[List[int], List[str]]:
    """Read integers from a text file and keep running on invalid rows.

    Args:
        file_path (str): Path to the input file.

    Returns:
        Tuple[List[int], List[str]]: A tuple (integers, issues) where integers are
        successfully parsed values and issues are warnings/errors to display.
    """
    integers: List[int] = []
    issues: List[str] = []

    try:
        with open(file_path, "r", encoding="utf-8") as input_file:
            for row_index, raw_line in enumerate(input_file, start=1):
                clean_text = raw_line.strip()
                if not clean_text:
                    issues.append(f"Line {row_index}: empty line (skipped)")
                    continue
                try:
                    integers.append(int(clean_text))
                except ValueError:
                    issues.append(
                        f"Line {row_index}: invalid integer '{clean_text}' (skipped)"
                    )
    except FileNotFoundError:
        issues.append(f"File not found: {file_path}")
    except OSError as exc:
        issues.append(f"Could not read file '{file_path}': {exc}")

    return integers, issues


def convert_to_base(value: int, base: int) -> str:
    """Convert an integer to base 2..16 using repeated division.

    Args:
        value (int): Integer to convert.
        base (int): Target base (2 to 16).

    Returns:
        str: Converted value using digits 0-9 and A-F.

    Raises:
        ValueError: If base is not between 2 and 16.
    """
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16")

    if value == 0:
        return "0"

    sign = ""
    magnitude = value
    if magnitude < 0:
        sign = "-"
        magnitude = -magnitude

    digits: List[str] = []
    while magnitude > 0:
        remainder = magnitude % base
        digits.append(HEX_SYMBOLS[remainder])
        magnitude //= base

    converted = ""
    for i in range(len(digits) - 1, -1, -1):
        converted += digits[i]

    return sign + converted


def write_output_file(lines: List[str]) -> None:
    """Write the output lines to the required results file.

    Args:
        lines (List[str]): Lines to write to the output file.
    """
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        for line in lines:
            output_file.write(line + "\n")


def main(argv: List[str]) -> int:
    """Entry point for command-line execution.

    Args:
        argv (List[str]): Command-line arguments (expects input file path).

    Returns:
        int: Exit code (0 on success).
    """
    if len(argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return 2

    input_path = argv[1]
    start_time = time.perf_counter()

    integers, issues = read_integer_values(input_path)
    for msg in issues:
        print(f"ERROR: {msg}")

    output_lines: List[str] = ["ITEM\tDEC\tBIN\tHEX"]
    item_index = 1

    for number in integers:
        binary_text = convert_to_base(number, 2)
        hex_text = convert_to_base(number, 16)
        output_lines.append(f"{item_index}\t{number}\t{binary_text}\t{hex_text}")
        item_index += 1

    elapsed = time.perf_counter() - start_time
    output_lines.append(f"Time Elapsed (s):\t{elapsed:.6f}")

    for line in output_lines:
        print(line)

    write_output_file(output_lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

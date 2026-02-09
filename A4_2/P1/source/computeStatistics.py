#!/usr/bin/env python3
"""
computeStatistics.py

Reads a text file with numeric values (one per line). Computes descriptive
statistics using basic algorithms (no numpy/statistics): mean, median, mode,
population variance and population standard deviation.

Outputs results to console and to StatisticsResults.txt, and logs invalid
lines while continuing execution. Reports elapsed execution time at the end.
"""

from __future__ import annotations

import sys
import time
from typing import List, Optional, Tuple


OUTPUT_FILENAME = "StatisticsResults.txt"


def read_numeric_values(file_path: str) -> Tuple[List[float], List[str]]:
    """Return (values, issues) while keeping the program running on bad rows."""
    numeric_values: List[float] = []
    issues: List[str] = []

    try:
        with open(file_path, "r", encoding="utf-8") as input_file:
            for row_index, raw_line in enumerate(input_file, start=1):
                clean_text = raw_line.strip()
                if not clean_text:
                    issues.append(f"Line {row_index}: empty line (skipped)")
                    continue
                try:
                    numeric_values.append(float(clean_text))
                except ValueError:
                    issues.append(
                        f"Line {row_index}: invalid number '{clean_text}' (skipped)"
                    )
    except FileNotFoundError:
        issues.append(f"File not found: {file_path}")
    except OSError as exc:
        issues.append(f"Could not read file '{file_path}': {exc}")

    return numeric_values, issues


def selection_sort(values: List[float]) -> List[float]:
    """Basic sorting algorithm: selection sort (returns a sorted copy)."""
    sorted_copy = values[:]
    total_items = len(sorted_copy)

    for i in range(total_items):
        smallest_pos = i
        for j in range(i + 1, total_items):
            if sorted_copy[j] < sorted_copy[smallest_pos]:
                smallest_pos = j
        sorted_copy[i], sorted_copy[smallest_pos] = sorted_copy[smallest_pos], sorted_copy[i]

    return sorted_copy


def compute_mean(values: List[float]) -> float:
    total_sum = 0.0
    for val in values:
        total_sum += val
    return total_sum / len(values)


def compute_median(values: List[float]) -> float:
    sorted_values = selection_sort(values)
    count = len(sorted_values)
    middle = count // 2

    if count % 2 == 1:
        return sorted_values[middle]
    return (sorted_values[middle - 1] + sorted_values[middle]) / 2.0


def compute_mode(values: List[float]) -> Optional[float]:
    """
    Returns:
      - None if all values appear only once.
      - If multiple modes, returns the smallest mode for determinism.
    """
    frequency_map: dict[float, int] = {}
    for val in values:
        frequency_map[val] = frequency_map.get(val, 0) + 1

    best_frequency = 0
    best_value: Optional[float] = None

    for val, freq in frequency_map.items():
        if freq > best_frequency:
            best_frequency = freq
            best_value = val
        elif freq == best_frequency and best_value is not None and val < best_value:
            best_value = val

    if best_frequency <= 1:
        return None
    return best_value


def compute_population_variance(values: List[float]) -> float:
    mean_value = compute_mean(values)
    squared_sum = 0.0

    for val in values:
        delta = val - mean_value
        squared_sum += delta * delta

    return squared_sum / len(values)


def compute_population_stddev(values: List[float]) -> float:
    return compute_population_variance(values) ** 0.5


def build_output_text(
    item_count: int,
    mean_value: float,
    median_value: float,
    mode_value: Optional[float],
    stddev_value: float,
    variance_value: float,
    elapsed_seconds: float,
) -> str:
    mode_text = "N/A" if mode_value is None else f"{mode_value:.6f}"
    return (
        f"Count: {item_count}\n"
        f"Mean: {mean_value:.6f}\n"
        f"Median: {median_value:.6f}\n"
        f"Mode: {mode_text}\n"
        f"Standard Deviation (Population): {stddev_value:.6f}\n"
        f"Variance (Population): {variance_value:.6f}\n"
        f"Time Elapsed (s): {elapsed_seconds:.6f}\n"
    )


def write_output_file(text: str) -> None:
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        output_file.write(text)


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return 2

    input_path = argv[1]
    start_time = time.perf_counter()

    values, issues = read_numeric_values(input_path)
    for msg in issues:
        print(f"ERROR: {msg}")

    elapsed = time.perf_counter() - start_time

    if not values:
        empty_text = f"No valid numbers to process.\nTime Elapsed (s): {elapsed:.6f}\n"
        print(empty_text, end="")
        write_output_file(empty_text)
        return 1

    mean_value = compute_mean(values)
    median_value = compute_median(values)
    mode_value = compute_mode(values)
    variance_value = compute_population_variance(values)
    stddev_value = compute_population_stddev(values)

    elapsed = time.perf_counter() - start_time
    output_text = build_output_text(
        item_count=len(values),
        mean_value=mean_value,
        median_value=median_value,
        mode_value=mode_value,
        stddev_value=stddev_value,
        variance_value=variance_value,
        elapsed_seconds=elapsed,
    )

    print(output_text, end="")
    write_output_file(output_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

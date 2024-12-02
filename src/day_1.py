from collections import Counter
from re import split

from common.input import read_to_string


def part_1(input: list[int]) -> int:
    return sum(
        [
            abs(r_element - l_element)
            for l_element, r_element in zip(sorted(input[::2]), sorted(input[1::2]), strict=True)
        ]
    )


def part_2(input: list[int]) -> int:
    r_counter = Counter(input[1::2])
    return sum([l_element * r_counter[l_element] for l_element in input[::2]])


if __name__ == "__main__":
    input = list(map(int, split(r"   |\n", read_to_string("src/data/day_1"))))
    print(f"Day 1 Part 1: {part_1(input)}\nDay 1 Part 2: {part_2(input)}")

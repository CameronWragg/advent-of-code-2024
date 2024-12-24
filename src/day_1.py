from collections import Counter
from re import split

from common.inputs import read_to_string


def part_1(data: list[int]) -> int:
    return sum(
        [
            abs(r_element - l_element)
            for l_element, r_element in zip(sorted(data[::2]), sorted(data[1::2]), strict=True)
        ],
    )


def part_2(data: list[int]) -> int:
    r_counter = Counter(data[1::2])
    return sum([l_element * r_counter[l_element] for l_element in data[::2]])


if __name__ == "__main__":
    data = list(map(int, split(r"   |\n", read_to_string("src/data/day_1"))))
    print(f"Day 1 Part 1: {part_1(data)}\nDay 1 Part 2: {part_2(data)}")

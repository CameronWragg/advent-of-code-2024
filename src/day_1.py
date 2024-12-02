from re import split

from common.input import read_to_string


def part_1():
    input = split(r"   |\n", read_to_string("src/data/day_1"))
    return sum(
        [
            abs(int(r_element) - int(l_element))
            for l_element, r_element in zip(sorted(input[::2]), sorted(input[1::2]), strict=True)
        ]
    )


if __name__ == "__main__":
    print(f"Day 1 Part 1: {part_1()}")

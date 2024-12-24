def read_to_string(file_location: str) -> str:
    return open(file_location).read().rstrip("\n")


def read_to_list(file_location: str, to_int: bool, separator: str) -> list[str] | list[int]:
    _list = read_to_string(file_location).split(separator)

    if to_int:
        return [int(element.rstrip("\n")) for element in _list]

    return _list

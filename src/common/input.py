def read_to_string(file_location: str) -> str:
    return open(file_location).read().rstrip("\n")

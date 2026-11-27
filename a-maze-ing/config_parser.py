
from dataclasses import dataclass


REQUIRED_KEYS = (
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
)


@dataclass
class MazeConfig:
    width: int
    height: int
    entry_coords: tuple[int, int]
    exit_coords: tuple[int, int]
    output_file: str
    perfect: bool


# - PARSING HELPERS

def parse_dimensions(value: str, key: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{key}: '{value}' is not a valid integer")

    if number <= 0:
        raise ValueError(f"{key}: must be greater than 0 (got {number})")
    return number


def parse_coords(
        value: str, key: str, width: int, height: int
) -> tuple[int, int]:
    if value.count(",") != 1:
        raise ValueError(f"{key}: expected 'x, y' format (got '{value}')")

    raw_x, raw_y = value.split(",")
    try:
        x = int(raw_x.strip())
        y = int(raw_y.strip())
    except ValueError:
        raise ValueError(
                f"{key}: coordinates must be integers (got '{value}')"
        )

    if not (0 <= x < width and 0 <= y < height):
        raise ValueError(
            f"{key}: ({x}, {y}) is out of bounds for {width}x{height} maze"
        )

    return (x, y)


def parse_bool(value: str, key: str) -> bool:
    lowered = value.lower()

    if lowered == "true":
        return True
    if lowered == "false":
        return False

    raise ValueError(f"{key}: expected 'True' or 'False' (got '{value}')")


# - PARSING

def parse_config(filepath: str) -> MazeConfig:
    str_config: dict[str, str] = {}

    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"file '{filepath}' not found")
    except PermissionError:
        raise PermissionError(f"permission denied for '{filepath}'")
    except IsADirectoryError:
        raise IsADirectoryError(f"'{filepath}' is a directory")
    except OSError as err:
        raise OSError(f"cannot read '{filepath}': {err.strerror}")

    # Check line syntax, unknown keys, duplicate keys
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.count("=") != 1:
            raise ValueError(
                    f"Line {line_number}: expected a single '=' -> '{line}'"
                    )

        key, value = line.split("=")
        key = key.strip()
        value = value.strip()

        if key not in REQUIRED_KEYS:
            raise ValueError(f"Line {line_number}: unknown key '{key}'")
        if key in str_config:
            raise ValueError(f"Line {line_number}: duplicate key '{key}'")

        str_config[key] = value

    # Check missing keys
    missing: list[str] = []
    for key in REQUIRED_KEYS:
        if key not in str_config:
            missing.append(key)
    if missing:
        raise ValueError(f"Missing required keys: {', '.join(missing)}")

    # Validation and conversion values

    width = parse_dimensions(str_config["WIDTH"], "WIDTH")
    height = parse_dimensions(str_config["HEIGHT"], "HEIGHT")

    entry_coords = parse_coords(str_config["ENTRY"], "ENTRY", width, height)
    exit_coords = parse_coords(str_config["EXIT"], "EXIT", width, height)
    if entry_coords == exit_coords:
        raise ValueError(
                f"ENTRY and EXIT cannot be the same cell {entry_coords}"
        )

    perfect = parse_bool(str_config["PERFECT"], "PERFECT")

    output_file = str_config["OUTPUT_FILE"]
    if not output_file.endswith(".txt") or output_file == ".txt":
        raise ValueError(
                f"OUTPUT_FILE: "
                f"must be a valid .txt filename (got '{output_file}')"
        )

    return MazeConfig(
        width=width,
        height=height,
        entry_coords=entry_coords,
        exit_coords=exit_coords,
        output_file=output_file,
        perfect=perfect,
    )

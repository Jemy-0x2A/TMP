
from mazegen.generator import MazeGenerator


WALL_COLORS: dict[str, str] = {
    "W": "\033[1;37m",  # White
    "C": "\033[1;34m",  # Blue
    "Y": "\033[2;33m",  # Yellow
    "G": "\033[1;38;5;28m",  # Green
    "M": "\033[1;35m",  # Magenta
}

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

CLEAN_SCREEN = "\033[H\033[2J\033[3J"


def print_maze(
    grid: list[list[int]],
    entry_pos: tuple[int, int],
    exit_pos: tuple[int, int],
    logo_coords: set[tuple[int, int]] | None,
    solution_coords: list[tuple[int, int]] | None,
    color_key: str
) -> None:

    height = len(grid)
    width = len(grid[0])
    logo = logo_coords if logo_coords else set()
    path = set(solution_coords) if solution_coords else set()
    color = WALL_COLORS[color_key]

    print(CLEAN_SCREEN, end="", flush=True)

    top_line = f"{color}+" + "---+" * width + RESET
    print(top_line)

    for y in range(height):
        mid_line = f"{color}|{RESET}"
        bottom_line = f"{color}+{RESET}"

        for x in range(width):
            cell = grid[y][x]

            if (x, y) in logo:
                body = f"{color}███{RESET}"
            elif (x, y) == entry_pos:
                body = f"{GREEN}███{RESET}"
            elif (x, y) == exit_pos:
                body = f"{RED}███{RESET}"
            elif (x, y) in path:
                body = f"{CYAN} • {RESET}"
            else:
                body = "   "

            east_wall = (
                f"{color}|{RESET}"
                if (cell & MazeGenerator.EAST) else " "
            )
            mid_line += body + east_wall

            south_wall = (
                f"{color}---{RESET}"
                if (cell & MazeGenerator.SOUTH) else "   "
            )
            bottom_line += south_wall + f"{color}+{RESET}"

        print(mid_line)
        print(bottom_line)

import random

class MazeGenerator:
    NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8
    ALL_WALLS = 15

    DIRECTIONS = {
            "N": (0, -1, NORTH, SOUTH),
            "E": (1, 0, EAST, WEST),
            "S": (0, 1, SOUTH, NORTH),
            "W": (-1, 0, WEST, EAST),
    }

    ORIENTATION: dict[tuple[int, int], str] = {
            (0, -1): "N",
            (1, 0): "E",
            (0, 1): "S",
            (-1, 0): "W",
    }

    def __init__(
            self,
            width: int,
            height: int,
            entry_pos: tuple[int, int],
            exit_pos: tuple[int, int],
            perfect: bool
    ) -> None:

        self.width = width
        self.height = height
        self.entry_pos = entry_pos
        self.exit_pos = exit_pos
        self.perfect = perfect

        self.grid: list[list[int]] = []
        self.logo_coords: set[tuple[int, int]] = self._generate_logo()
        self.solution_coords: list[tuple[int, int]] = []

        #self.solution_path: str = ""
        #self.hex_grid: str = ""

        self.generate()

# - LOGO 42

    def _generate_logo(self) -> set[tuple[int, int]]:
        logo = [
                "#.#.###",
                "#.#...#",
                "###.###",
                "..#.#..",
                "..#.###",
                ]
        logo_height = len(logo)
        logo_width = len(logo[0])
        margin = 3

        if (
                self.width < logo_width + (margin * 2)
                or self.height < logo_height + (margin * 2)
        ):
            return set()

        start_x = (self.width - logo_width) // 2
        start_y = (self.height - logo_height) // 2

        coords_logo: set[tuple[int, int]] = set()
        for direction_y, row in enumerate(logo):
            for direction_x, col in enumerate(row):
                if col == "#":
                    coords_logo.add((start_x + direction_x, start_y + direction_y))

        return coords_logo

# - GENERATION HELPERS

    def _next_coords_are_valid(
            self,
            coords: tuple[int, int],
            direction: str
    ) -> bool:
        x, y = coords
        direction_x, direction_y, _, _ = self.DIRECTIONS[direction]

        next_x = x + direction_x
        next_y = y + direction_y

        # Check grid limits, 42 logo, and already opened cells
        if not (0 <= next_x < self.width and 0 <= next_y < self.height):
            return False
        if (next_x, next_y) in self.logo_coords:
            return False
        if self.grid[next_y][next_x] != self.ALL_WALLS:
            return False

        return True

    def _break_wall(
            self,
            coords: tuple[int, int],
            direction: str
    ) -> tuple[int, int]:
        x, y = coords
        direction_x, direction_y, current_wall, opposite_wall = self.DIRECTIONS[direction]

        next_x = x + direction_x
        next_y = y + direction_y

        self.grid[y][x] &= ~current_wall
        self.grid[next_y][next_x] &= ~opposite_wall

        return (next_x, next_y)

# - GENERATION

    def generate(self) -> list[list[int]]:
        self.grid = [[self.ALL_WALLS] * self.width for _ in range(self.height)]
        path_stack = [(0, 0)]
        actual_direction: str | None = None

        while path_stack:
            valids_directions: list[str] = []
            actual_coords = path_stack[-1]

            if not actual_direction:
                valids_directions = [
                        direction
                        for direction in self.DIRECTIONS.keys()
                        if self._next_coords_are_valid(actual_coords, direction)
                        ]

                if valids_directions:
                    actual_direction =  random.choice(valids_directions)
                else:
                    path_stack.pop()
                    continue

            else:
                if not self._next_coords_are_valid(actual_coords, actual_direction):
                    actual_direction = None
                    continue

            next_coords = self._break_wall(actual_coords, actual_direction)
            path_stack.append(next_coords)

            if random.random() < 0.6:
                actual_direction = None

        #self.hex_grid = self._grid_to_hex()
        self._solve()
        #self.solution_path = self._path_to_directions()
        return self.grid

# - SOLVING HELPER

    def _get_valid_next_cells(
        self,
        current_cell: tuple[int, int],
        came_from: dict[tuple[int, int], tuple[int, int] | None],
    ) -> list[tuple[int, int]]:
        x, y = current_cell
        next_valid_cells: list[tuple[int, int]] = []

        for direction_x, direction_y, wall_mask, _ in self.DIRECTIONS.values():
            if not (self.grid[y][x] & wall_mask):
                next_cell = (x + direction_x, y + direction_y)
                if next_cell not in came_from:
                    next_valid_cells.append(next_cell)

        return next_valid_cells

# - SOLVING

    def _solve(self) -> None:
        queue: list[tuple[int, int]] = [self.entry_pos]
        came_from: dict[tuple[int, int], tuple[int, int] | None] = {
            self.entry_pos: None
        }

        if self.entry_pos != self.exit_pos:
            exit_found = False
        else:
            exit_found = True

        while not exit_found:
            if not queue:
                raise ValueError("Maze has no valid path from entry to exit")

            current_cell = queue.pop(0)
            next_cells = self._get_valid_next_cells(current_cell, came_from)

            for cell in next_cells:
                queue.append(cell)
                came_from[cell] = current_cell
                if cell == self.exit_pos:
                    exit_found = True
                    break

        solution: list[tuple[int, int]] = []
        current_coords: tuple[int, int] | None = self.exit_pos

        while current_coords is not None:
            solution.append(current_coords)
            current_coords = came_from[current_coords]

        solution.reverse()
        self.solution_coords = solution

# - OUTPUT: HEXA + ENTRY/EXIT + PATH(N, S, E, W)

# HELPERS

    def _grid_to_hex(self) -> str:
        hex_grid: list[list[str]] = [
            [format(cell, "X") for cell in row]
            for row in self.grid
        ]

        hex_rows: list[str] = ["".join(row) for row in hex_grid]

        return "\n".join(hex_rows)

    def _coords_to_directions(self) -> str:
        directions: list[str] = []

        for (x1, y1), (x2, y2) in zip(self.solution_coords, self.solution_coords[1:]):
            direction = (x2 - x1, y2 - y1)
            directions.append(self.ORIENTATION[direction])

        return "".join(directions)

# FUNCTION

    def format_output(self) -> str:
        hex_grid = self._grid_to_hex()
        entry_str = f"{self.entry_pos[0]},{self.entry_pos[1]}"
        exit_str = f"{self.exit_pos[0]},{self.exit_pos[1]}"
        solution_path = self._coords_to_directions()

        return (
            f"{hex_grid}\n\n"
            f"{entry_str}\n"
            f"{exit_str}\n"
            f"{solution_path}\n"
        )

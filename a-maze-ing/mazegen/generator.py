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
        self.grid = [[self.ALL_WALLS] * self.width for _ in range(self.height)]
        self.logo_coords: set[tuple[int, int]] = self._generate_logo()

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

# - FONCTIONS TOOLS

    def _next_coords_are_valids(self, coords: tuple[int, int], direction: str) -> bool:
        x, y = coords
        direction_x, direction_y = self.DIRECTIONS[direction][:2]

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

    def _break_wall(self, coords: tuple[int, int], direction: str) -> tuple[int, int]:
        x, y = coords
        direction_x, direction_y, current_wall, opposite_wall = self.DIRECTIONS[direction]

        next_x = x + direction_x
        next_y = y + direction_y

        self.grid[y][x] &= ~current_wall
        self.grid[next_y][next_x] &= ~opposite_wall

        return (next_x, next_y)


# - GENERATE

    def generate(self) -> list[list[int]]:
        path_stack = [(0, 0)]
        actual_direction: str | None = None
        all_directions = [direction for direction in self.DIRECTIONS.keys()]

        while path_stack:
            valids_directions: list[str] = []
            actual_coords = path_stack[-1]

            if not actual_direction:
                valids_directions = [
                        direction
                        for direction in all_directions
                        if self._next_coords_are_valids(actual_coords, direction)
                        ]

                if valids_directions:
                   actual_direction =  random.choice(valids_directions)
                else:
                    path_stack.pop()
                    continue

            else:
                if not self._next_coords_are_valids(actual_coords, actual_direction):
                    actual_direction = None
                    continue

            next_coords = self._break_wall(actual_coords, actual_direction)
            path_stack.append(next_coords)

            if random.random() < 0.6:
                actual_direction = None

        return self.grid

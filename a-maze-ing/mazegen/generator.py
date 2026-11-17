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
        self.grid = [[15] * self.width for _ in range(self.height)]

    def generate(self) -> list[list[int]]:
        path_stack = [self.entry_pos]
        actual_direction: str | None = None
        all_directions = [direction for direction in self.DIRECTIONS.keys()]

        while path_stack:
            valids_directions: list[str] = []
            actual_coords = path_stack[-1]

            if not actual_direction:
                valids_directions = [
                        direction
                        for direction in all_directions
                        if next_coords_are_valids(actual_coords, direction)
                        ]

                if valids_directions:
                   actual_direction =  random.choice(valids_directions)
                else:
                    path_stack.pop()
                    continue

            else:
                if not next_coords_are_valids(actual_coords, actual_direction):
                    actual_direction = None
                    continue

            next_coords = break_wall(actual_coords, actual_direction)
            path_stack.append(next_coords)
            
            if random.random() < 0.2:
                actual_direction = None

        return self.grid

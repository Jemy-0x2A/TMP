
import sys
from config_parser import parse_config
from mazegen.generator import MazeGenerator
from display import print_maze


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>", file=sys.stderr)
        sys.exit(1)

    try:
        config = parse_config(sys.argv[1])
    except (OSError, ValueError) as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    maze = MazeGenerator(
        width=config.width,
        height=config.height,
        entry_pos=config.entry_coords,
        exit_pos=config.exit_coords,
        perfect=config.perfect,
    )

    show_path = False
    colors = ["W", "C", "Y", "G", "M"]
    color_index = 0

    while True:
        print_maze(
            maze.grid,
            maze.entry_pos,
            maze.exit_pos,
            maze.logo_coords,
            maze.solution_coords if show_path else None,
            colors[color_index]
        )
        
        # Test temporaire pour vérifier que tout est bien chargé
        print(f"Loaded config: {config}")
        
        print(
                "\n=== A-Maze-ing ===\n"
                "1. Re-generate a new maze\n"
                "2. Show/Hide path from entry to exit\n"
                "3. Rotate maze colors\n"
                "4. Quit\n"
              )
        choice = input("Choice? (1-4): ")

        if choice == "1":
            maze.generate()
        elif choice == "2":
            show_path = not show_path
        elif choice == "3":
            color_index = (color_index + 1) % len(colors)
        elif choice == "4":
            break
        else:
            continue

if __name__ == "__main__":
    main()

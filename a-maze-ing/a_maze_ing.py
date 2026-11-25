#lecture du fichier de configuration et recuperation des parametre

#-re/generer et ecrire la chaine hexa de svg dans le fichier sortie
#-afficher/masquer chemin
#-changer la couleur des murs
#-quitter

from mazegen.generator import MazeGenerator
from display import print_maze


def main() -> None:
    maze = MazeGenerator(
        width=21,
        height=19,
        entry_pos=(2, 2),
        exit_pos=(18, 16),
        perfect=True,
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

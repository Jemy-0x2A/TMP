#lecture du fichier de configuration et recuperation des parametre

#boucle affichage et interaction 
#-re/generer et ecrire la chaine hexa de svg dans le fichier sortie
#-afficher/masquer chemin
#-changer la couleur des murs
#-quitter

from mazegen.generator import MazeGenerator

def print_maze(
    grid: list[list[int]],
    entry_pos: tuple[int, int],
    exit_pos: tuple[int, int],
    logo_coords: set[tuple[int, int]] | None = None,
) -> None:
    height = len(grid)
    width = len(grid[0])
    blocked = logo_coords or set()

    # Mur tout en haut du labyrinthe
    print("+" + "---+" * width)

    for y in range(height):
        row_cells = "|"
        row_bottom = "+"

        for x in range(width):
            cell = grid[y][x]

            # Contenu de la case (Logo, Entrée, Sortie ou vide)
            if (x, y) in blocked:
                body = "\033[97m███\033[0m"
            elif (x, y) == entry_pos:
                body = " E "
            elif (x, y) == exit_pos:
                body = " S "
            else:
                body = "   "

            # Mur Est (bit 2)
            east_wall = "|" if (cell & MazeGenerator.EAST) else " "
            row_cells += body + east_wall

            # Mur Sud (bit 4)
            south_wall = "---" if (cell & MazeGenerator.SOUTH) else "   "
            row_bottom += south_wall + "+"

        print(row_cells)
        print(row_bottom)


if __name__ == "__main__":
    maze = MazeGenerator(
        width=21,
        height=19,
        entry_pos=(2, 2),
        exit_pos=(18, 16),
        perfect=True,
    )
    grid = maze.generate()

    print("Grille brute (bitmasks) :")
    for row in grid:
        print(row)

    print("\nRendu visuel :")
    print_maze(grid, maze.entry_pos, maze.exit_pos, maze.logo_coords)

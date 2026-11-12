import random

TAILLE = 15
# On initialise tout à 0 (Roche blanche)
grille = [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]

# 1. On applique votre idée : On pose les bordures "2" tout autour
for y in range(TAILLE):
    for x in range(TAILLE):
        if x == 0 or x == TAILLE - 1 or y == 0 or y == TAILLE - 1:
            grille[y][x] = 2  # 2 = Bordure / Mur extérieur incassable

# Point de départ
depart_x, depart_y = 1, 1
grille[depart_y][depart_x] = 1
stack = [(depart_x, depart_y)]

# 2. La validation simplifiée grâce au chiffre 2 !
def case_suivante_est_valide(x, y, dir_x, dir_y):
    cible_x = x + dir_x
    cible_y = y + dir_y
    
    # Si la cible est une bordure (2) ou déjà un chemin (1), c'est mort
    if grille[cible_y][cible_x] != 0:
        return False
        
    # REGLE D'OR : On compte combien de '1' (chemins) touchent la case cible
    directions_voisins = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nb_chemins_autour = 0
    
    for vx, vy in directions_voisins:
        if grille[cible_y + vy][cible_x + vx] == 1:
            nb_chemins_autour += 1
            
    # La case n'est valide que si le SEUL '1' autour d'elle est la case d'où l'on vient (donc le compteur vaut exactement 1)
    return nb_chemins_autour == 1

# 3. La boucle de déplacement (La même logique "ligne droite")
direction_actuelle = None

while len(stack) > 0:
    actuel_x, actuel_y = stack[-1]
    toutes_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # Haut, Bas, Gauche, Droite
    
    if direction_actuelle is None:
        choix_valides = [d for d in toutes_directions if case_suivante_est_valide(actuel_x, actuel_y, d[0], d[1])]
        if choix_valides:
            direction_actuelle = random.choice(choix_valides)
        else:
            stack.pop() # Cul-de-sac -> on recule
            continue

    dx, dy = direction_actuelle
    if case_suivante_est_valide(actuel_x, actuel_y, dx, dy):
        prochain_x, prochain_y = actuel_x + dx, actuel_y + dy
        grille[prochain_y][prochain_x] = 1
        stack.append((prochain_x, prochain_y))
        
        if random.random() < 0.20: # 20% de chance de vouloir tourner
            direction_actuelle = None
    else:
        direction_actuelle = None

# 4. Affichage mis à jour pour voir la bordure
def afficher_grille(matrice):
    for ligne in matrice:
        chars = []
        for case in ligne:
            if case == 2:
                chars.append("🔴") # Le 2 (Bordure) en Rouge pour bien la voir
            elif case == 0:
                chars.append("██") # Le 0 (Roche) en Blanc
            else:
                chars.append("  ") # Le 1 (Chemin) en Noir (Vide)
        print("".join(chars))

afficher_grille(grille)


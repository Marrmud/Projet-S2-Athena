import time
import sys
#Initialisation...#
#==========================================================================================
liste_D = [['o', 'o', 'o', '•', '•'], ['o', 'o', 'o', '•', '•'],
           ['o', 'o', ' ', '•', '•'], ['o', 'o', '•', '•', '•'],
           ['o', 'o', '•', '•', '•']]

liste_M = [[' ', '•', '•', 'o', ' '], ['•', 'o', ' ', ' ', 'o'],
           ['•', '•', 'o', ' ', 'o'], ['•', ' ', 'o', ' ', 'o'],
           [' ', '•', 'o', '•', 'o']]

liste_F = [['•', ' ', ' ', ' ', 'o'], [' ', '•', ' ', ' ', ' '],
           [' ', 'o', ' ', ' ', ' '], [' ', ' ', 'o', ' ', ' '],
           [' ', ' ', ' ', 'o', ' ']]

lettre = ["A ∥ ", "B ∥ ", "C ∥ ", "D ∥ ", "E ∥ "]

bol = 0



#==========================================================================================
#Affichage
def simple_dash():
    return ("---------------------------------")
def double_dash():
    return ("♠================================♠")

#Afficher Grille
def afficher_grille(liste):
    print(double_dash())
    print("      1", " ∥  2", " ∥  3", " ∥  4", " ∥  5")
    print(" ---------------------------------")
    for ligne in range(len(liste)):
      print(lettre[ligne], end="  ")
      for colonne in range(len(liste[ligne])):
          print(liste[ligne][colonne], end="  |  ")
      print('\n', simple_dash())
    print(double_dash())
    return('')

#GRILLE CHOIX#
def choix_grille_afficher(liste_D, liste_M, liste_F):
    print('\n')
    print('''
⌈ D pour le sénario de Début  ⌉
  M pour le sénario du Milieu  
⌊ F pour le sénario de Fin    ⌋
  ''')
    print('\n')
    time.sleep(1.0)
    choix = str(input("Choisissez grille: "))
    if choix == 'D':
      print(afficher_grille(liste_D))
      return (selection_pion_grille(liste_D))
    if choix == 'M':
      print(afficher_grille(liste_M))
      return (selection_pion_grille(liste_M))
    if choix == 'F':
      print(afficher_grille(liste_F))
      return (selection_pion_grille(liste_F))
    else:
      print("Entez valeur valide (D, M, F)\n")
      return choix_grille_afficher(liste_D, liste_M, liste_F)


#==========================================================================================

###fonctions de verification

#Les deux fonctions suivantes sont la division de la fonction est_dans_grille en une fonction ligne_est_dans_grille et colonne_est_dans_grille.


#vérification si ligne est_dans_grille.
def ligne_est_dans_grille():
    Liste_ligne = ["A", "B", "C", "D", "E"]
    while True:
        ligne = str(input("Entrez ligne: "))
        if not Liste_ligne.count(ligne) == 0:
            return ligne


#vérification si colonne est_dans_grille.
def colonne_est_dans_grille():
    Liste_colonne = ["1", "2", "3", "4", "5"]
    while True:
        colonne = str(input("Entrez colonne: "))
        if not Liste_colonne.count(colonne) == 0:
            print("\n")
            return colonne

#==========================================================================================

#Conversion ligne en int
def choix_pion_ligne(ligne):
    if ligne == 'A':
        ligne = 0
    elif ligne == 'B':
        ligne = 1
    elif ligne == 'C':
        ligne = 2
    elif ligne == 'D':
        ligne = 3
    elif ligne == 'E':
        ligne = 4
    return (ligne)

              
#Quitter
def choix_quitter(liste_D, liste_M, liste_F):
  print("Quitter ?\n")
  print('''
_____________
  Y pour Oui
  N pour Non
_____________
  ''')
  val = str(input("⤇ "))
  if val == 'N':
    return choix_grille_afficher(liste_D, liste_M, liste_F)
  elif val == 'Y':
    time.sleep(1.0)
    print("A Bientôt...")
    time.sleep(1.0)
    sys.exit()

#Peut bouger

#Deplacement
def deplacement(liste, ligne, colonne):
  time.sleep(0.5)
  print('\n')
  print("Veuillez choisir une case d'arivée :")
  print('\n')
  time.sleep(0.5)
  ligne_move = choix_pion_ligne(ligne_est_dans_grille())
  colonne_move = int(colonne_est_dans_grille()) - 1
  if (abs(ligne - ligne_move) + abs(colonne - colonne_move)) == 1 or (
          abs(colonne_move - colonne) == abs(ligne_move - ligne)) and (
              (abs(colonne_move - colonne) + abs(ligne_move - ligne)) == 2):
      if liste[ligne_move][colonne_move] == ' ':
          liste[ligne][colonne], liste[ligne_move][colonne_move] = liste[ligne_move][colonne_move], liste[ligne][colonne]
      return afficher_grille(liste)

  else:
      print("Case non valide...")
      time.sleep(1.0)
      return (deplacement(liste, ligne, colonne))
  



def selection_pion_grille(liste):
  ligne = choix_pion_ligne(ligne_est_dans_grille())
  colonne = int(colonne_est_dans_grille()) - 1
  if liste[ligne][colonne] == ' ':
    print('\n')
    print("Pion non valide !")
    print('\n')
    return (selection_pion_grille(liste))
  else:
    if liste[ligne][colonne] == '•':
      print('\n')
      time.sleep(1.0)
      print("Vous avez choisis : 'Pions noir' ")
      liste[ligne][colonne] = '♛'
      print('\n')
      time.sleep(0.5)
      print("Vous êtes : '♛'")
      time.sleep(0.5)
      print('\n')
      print(
          afficher_grille(liste),
          deplacement(liste, ligne, colonne))
      return ("")
  if liste[ligne][colonne] == 'o':
      print('\n')
      time.sleep(1.0)
      print("Vous avez choisis : 'Pions Blanc' ")
      liste[ligne][colonne] = '♕'
      print('\n')
      time.sleep(0.5)
      print("Vous êtes : '♕'")
      time.sleep(0.5)
      print('\n')
      print(
          afficher_grille(liste),
          deplacement(liste, ligne, colonne))
      return ("")


#jump
#can move

#==========================================================================================

#MENU#
def menu():
  val = input("Choisissez option 1, 2 ou 3: ")
  print('\n')
  if val == '1':
    return(choix_grille_afficher(liste_D, liste_M, liste_F))
  if val == '2':
    return("A venir :(")
  if val == '3':
    return(choix_quitter(liste_D, liste_M, liste_F))
  else :
    return menu()

print('''
        _   _                      
     /\  | | | |                     
    /  \ | |_| |__   ___ _ __   __ _ 
   / /\ \| __| '_ \ / _ \ '_ \ / _` |
  / ____ \ |_| | | |  __/ | | | (_| |
 /_/    \_\__|_| |_|\___|_| |_|\__,_|
                                     
                                     
Bienvenue...

===========================
-*-*-*-*-*-*-*-*-*-*-*-*-*-
        1 - Jouer
        2 - Tester
        3 - Quitter
-*-*-*-*-*-*-*-*-*-*-*-*-*-
===========================
  ''')
print(menu())


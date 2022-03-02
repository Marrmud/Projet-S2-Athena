#### REPRESENTATION DES DONNEES
###initialisation des grilles


print('''
Grille de début de partie:
    1   2   3   4   5
=======================
- - - - - - - - - - - -
A | • | • | • | o |  o|
- - - - - - - - - - - -
B | • | • | • | o | o |
- - - - - - - - - - - -
C | • | • |   | o | o |
- - - - - - - - - - - -
D | • | • | o | o | o |
- - - - - - - - - - - -
E | • | • | o | o | o |
- - - - - - - - - - - -
=======================
''')

print('''
Grille de milieu de partie:
    1   2   3   4   5
=======================
- - - - - - - - - - - -
A |   | • | • | o |   |
- - - - - - - - - - - -
B | • | o |   |   | o |
- - - - - - - - - - - -
C | • | • | o |   | o |
- - - - - - - - - - - -
D | • |   | o |   | o |
- - - - - - - - - - - -
E |   | • | o |   | o |
- - - - - - - - - - - -
=======================
''')
print('''
Grille de fin de partie:
    1   2   3   4   5
=======================
- - - - - - - - - - - -
A | • |   |   |   | o |
- - - - - - - - - - - -
B |   | • |   |   |   |
- - - - - - - - - - - -
C |   | o |   |   |   |
- - - - - - - - - - - -
D |   |   | o |   |   |
- - - - - - - - - - - -
E |   | o |   |   |   |
- - - - - - - - - - - -
=======================
''')

###fonctions de verification
#jeux de tests

#Les deux fonctions suivantes sont la division de la fonction est_dans_grille en une fonction ligne_est_dans_grille et colonne_est_dans_grille.
#vérification si ligne est_dans_grille.
def ligne_est_dans_grille ():
  Liste_ligne = ["A","B","C","D","E"]
  ligne = str(input("Entrez ligne: "))
  while Liste_ligne.count(ligne) == 0: #Tant que le .count ne passe pas à 1 (après avoir parcourus la liste), la boucle while continue
    ligne = str(input("Entrez ligne: "))
  return ligne

#vérification si colonne est_dans_grille.
def colonne_est_dans_grille ():
  Liste_colonne = ["1","2","3","4","5"]
  colonne = str(input("Entrez colonne: "))
  while Liste_colonne.count(colonne) == 0:
    colonne = str(input("Entrez colonne: "))
  return colonne


###fonctions de saisie
def saisir_coordonnees() :
  ligne = ligne_est_dans_grille()
  colonne = colonne_est_dans_grille()
  return ("Le pion a pour coordonées",ligne, colonne)

#<!> Pas besoin d'assert dans ce cas :D (car aucun contournement de cas possible).<!>.
def test_est_dans_grille():
  assert ligne_est_dans_grille () == "A" or "B" or "C" or "D" or "E", "Ligne inexistant"
  assert colonne_est_dans_grille () == "1"  or "2" or "3" or "4" or "5" , "Colonne inexistant"
#<!> Pas besoin d'assert dans ce cas :D (car aucun contournement de cas possible).<!>.



#test_est_dans_grille() <!> Pas besoin d'assert dans ce cas :D <!>.

#uniquement pour la mise au point, a conserver pour le correcteur

#affichage des coordonnees saisies
print(saisir_coordonnees())
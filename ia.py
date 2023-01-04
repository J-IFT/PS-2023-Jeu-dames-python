
def play(grille,premier_joueur):
	coups_valides = []
	for case in range (50):
		if(grille[case] == None):
			coups_valides.append(case)

	print(coups_valides)
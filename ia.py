import random

def play(grille,premier_joueur):
	if(premier_joueur):
		ia = 1
		joueur = 0
	else:
		ia = 0
		joueur = 1
	
	manger_dame = []
	manger_pion = []
	obtenir_dame = []
	deplacer_pion = []
	for case in range(50):
		case += 1
		# Priorité des coups :
		
		if(grille[case-1] == [ia, False] or grille[case-1] == [ia,True]):
			if(case%10 in [1,2,3,4,5]):
				increments = [5,6] if premier_joueur else [-5,-4]
			else:
				increments = [4,5] if premier_joueur else [-6,-5]

			#TODO géré les déplacements d'une dame (anvant et arriere)
			deplacements_possible = [] # Correspond aux deux cases ou peux se déplacer le pion
			if(case%10 != 6):
				incr = 9 if premier_joueur else -11
				if(case%10 == 1 or case+incr>50):
					deplacements_possible.append([case+increments[0],None])
				else:
					deplacements_possible.append([case+increments[0],case+incr])
			if(case%10 != 5):
				incr = 11 if premier_joueur else -9
				if(case%10 == 0 or case+incr>50):
					deplacements_possible.append([case+increments[1],None])
				else:
					deplacements_possible.append([case+increments[1],case+incr])

			for destination in deplacements_possible:
				if(destination[1] != None):
					if(grille[destination[0]-1]==[joueur,True] and grille[destination[1]-1] == None):
						# Manger une dame
						manger_dame.append([case,destination[1],destination[0]])
					if(grille[destination[0]-1] == [joueur,False] and grille[destination[1]-1] == None):
						# Manger un pion
						manger_pion.append([case, destination[1],destination[0]])
				if(destination[0] <= 50):
					ligne_fin = [46,47,48,49,50] if premier_joueur else [1,2,3,4,5]
					if(destination[0] in ligne_fin and grille[destination[0]-1] == None):
						# Obtenir une dame
						obtenir_dame.append([case,destination[0],'dame'])
					if(grille[destination[0]-1] == None):
						# bouger un pion
						deplacer_pion.append([case,destination[0],None])

	if(len(manger_dame)):
		return random.choice(manger_dame)
	elif(len(manger_pion)):
		return random.choice(manger_pion)
	elif(len(obtenir_dame)):
		return random.choice(obtenir_dame)
	elif(len(deplacer_pion)):
		return random.choice(deplacer_pion)
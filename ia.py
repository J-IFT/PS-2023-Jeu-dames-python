import random

def getDeplacementsPossibles(grille, case):
	deplacements = {
		'manger_dame'  : [],
		'manger_pion'  : [],
		'obtenir_dame' : [],
		'deplacer_pion': []
	}
	deplacements_v2 = {
		'manger_dame'  : [],
		'manger_pion'  : [],
		'obtenir_dame' : [],
		'deplacer_pion': []
	}
	case_dans_grille = grille[case-1]
	numero_ligne = (case-1)//5
	# print(case_dans_grille)
	if(case_dans_grille != None):
		increments = [] # Liste des incrments pour atteindre les case diagonaes +1 et +2
		increments_v2 = []
		direction = -1 if case_dans_grille[0] else 1
		if(case%10 in [1,2,3,4,5]):
			# Partie inférieur incréments 5 et 6
			increments_v2.append([-5, -6])
			increments_v2.append([-4, -5])
			increments_v2.append([+5, +4])
			increments_v2.append([+6, +5])
			
		else:
			# Partie supérieur incréments 4 et 5
			increments_v2.append([-6, -5])
			increments_v2.append([-5, -4])
			increments_v2.append([+4, +5])
			increments_v2.append([+5, +6])
		# print('   <dir:'+str(direction)+' case:'+str(case_dans_grille[0])+' '+str(increments)+'>')
		# print('   increments_v2: ' +str(increments_v2))
		# Verification si déplacement hors jeu
		
		for incr in increments_v2:
			# print(incr)
			# print((case+incr[0]-1)//5)
			# print(numero_ligne)
			if((case_dans_grille[0] == 1 and incr[0] > 0) or (case_dans_grille[0] == 0 and incr[0] < 0) or (case_dans_grille[1] == True)): 
				# Si joueur = 1 => noir  et c'est un pion on prend que les increments > 0
				# Si joueur = 0 => blanc et c'est un pion on prend que les increments < 0
				# Si c'est une dame
				if((case+incr[0]-1)//5 in [numero_ligne-1, numero_ligne+1] and (case+incr[0]) in range(1,51)):
					# Verif si que la destination soir bien sur une ligne adjacente
					if(grille[case+incr[0]-1] == None):
						if(case+incr[0] in [1,2,3,4,5,46,47,48,49,50] and grille[case-1][1] == False):
							# Verif si c'est la ligne de départ adverse
							deplacements_v2['obtenir_dame'].append([case, case+incr[0], -1])
						else:
							deplacements_v2['deplacer_pion'].append([case, case+incr[0]])
					elif(grille[case+incr[0]-1][0] != grille[case-1][0] and grille[case+incr[0]+incr[1]-1] == None and (case+incr[0]+incr[1]) in range(1,51)): 
						# Verif si la case destination est celle d'un pion adverse et celle d'apres est vide
						if((case+incr[0]+incr[1]-1)//5 in [numero_ligne+2,numero_ligne-2]):
							# Verif si la destination est bien sur une ligne +2 / -2
							if(grille[case+incr[0]-1][1] == True):
								# Verif si c'est une dame
								if(case+incr[0]+incr[1] in [1,2,3,4,5,46,47,48,49,50]):
									deplacements_v2['manger_dame'].append([case, case+incr[0]+incr[1], case+incr[0], -1])
								else:
									deplacements_v2['manger_dame'].append([case, case+incr[0]+incr[1], case+incr[0]])
							else:
								if(case+incr[0]+incr[1] in [1,2,3,4,5,46,47,48,49,50]):
									deplacements_v2['manger_pion'].append([case, case+incr[0]+incr[1], case+incr[0],-1])
								else:
									deplacements_v2['manger_pion'].append([case, case+incr[0]+incr[1], case+incr[0]])

		# print('   deplacements_v2: '+str(deplacements_v2))
		return deplacements_v2

def play(grille,joueur):
	#* joueur : 0 => blanc, 1 => noir
	manger_dame   = []   # 1
	manger_pion   = []   # 2
	obtenir_dame  = [] 	 # 3
	deplacer_pion = []	 # 4	
	for case in range(1,51):
		# print(str(grille[case-1])+str())
		if(grille[case-1] != None and grille[case-1][0] == joueur):
			deplacement = getDeplacementsPossibles(grille, case)
			# print('Case n°'+str(case)+' => '+str(deplacement))
			manger_dame += deplacement['manger_dame']
			manger_pion += deplacement['manger_pion']
			obtenir_dame += deplacement['obtenir_dame']
			deplacer_pion += deplacement['deplacer_pion']
	
	if(len(manger_dame)):
		return random.choice(manger_dame)
	elif(len(manger_pion)):
		return random.choice(manger_pion)
	elif(len(obtenir_dame)):
		return random.choice(obtenir_dame)
	elif(len(deplacer_pion)):
		return random.choice(deplacer_pion)
	else:
		print("C CASSé")
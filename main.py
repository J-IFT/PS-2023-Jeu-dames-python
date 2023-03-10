import tkinter as tk
import ia
import time

# Variables globales :
# - Joueur :
choixDeplacement = None
click = None
joueur = 1
coups = []
# - Common
timer = 0
vainceur = None

def afficher(plateau):
	print()
	j = 0
	for i, element in enumerate(plateau):
		if(element == None):
			pion = ' '
		elif(element[0] == 1):
			pion = 'N'
		elif(element[0] == 0):
			pion = 'B'
		
		i += 1
		
		if(i%10 != 6):
			print('| |'+str(pion), end='')
		else:
			print('|'+str(pion),end='')
		
		if(i%5 == 0 and i%10==5):
			print('|')
		if(i%5 == 0 and i%10==0):
			print('| |')

def getCoordonee(case):
	i = case-1
	if(int(i/5)%2 == 0):
		add = 1
	else:
		add = 0
	k = int(i/5)
	j = int(2*(i%5)+add)
	return [j,k]

def jouer(plateau,coup,canvas):
	if(len(coup) == 3):
		if(coup[2] == -1):
			# Nouvelle dame
			plateau[coup[0]-1][1] = True
		else:
			plateau[coup[2]-1]= None
	elif(len(coup) == 4):
		plateau[coup[0]-1][1] = True
		plateau[coup[2]-1]= None
	plateau[coup[1]-1] = plateau[coup[0]-1]
	plateau[coup[0]-1] = None
			
def iSvictoire(plateau):
	j1 = False
	j2 = False
	for i, element in enumerate(plateau):
		if(element != None):
			if(element[0] == 0):
				j1 = True
			if(element[0] == 1):
				j2 = True
	if((j1 or j2) and (j1 != j2)):
		if(j1):
			return 0
		if(j2):
			return 1
		else:
			return None
	else:
		return None

def afficher_plateau():

	# Créer une fenêtre tkinter
	fenetre = tk.Tk()
	fenetre.title("Jeu de Dames")

	# Créer un canvas dans la fenêtre pour dessiner le plateau de jeu
	canvas = tk.Canvas(fenetre, width=600, height=600)
	canvas.pack()

	# Dessiner le plateau de jeu en dessinant des carrés blancs et noirs
	plateau = 20*[[1,False]] + 10*[None] + 20*[[0,False]]
	# plateau = 20*[None] +[[0,False]]+ [[0,False]] + 1*[[1,False]] + 27*[None]
	# plateau = 30*[None]+20*[[0, False]]
	# plateau[32] = [1, False]
	# plateau[7] = [1, False]
	# plateau[12] = [0, False]
	# plateau[24] = [1, False]

	for i in range(10):
		for j in range(10):
			couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
			x1, y1 = i * 50, j * 50
			x2, y2 = x1 + 50, y1 + 50
			canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
	#TODO Affichage du nombre de piece mangé par chaque joueur (ou nb de piece restant sur le plateau)

	# Refresh des pions sur la grille
	def refresh(plateau,fenetre,canvas):
		for i, element in enumerate(plateau):
			if(int(i/5)%2 == 0):
				add = 1
			else:
				add = 0
			k = int(i/5)
			j = int(2*(i%5)+add)
			if(element != None):
				if(element[0] == 0):
					canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="black")
					# print(i,' : ',element)
					if(element[1] == True):
						canvas.create_oval(j * 50 + 15, k * 50 + 15, j * 50 + 35, k * 50 + 35, outline='white')
				else:
					canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="white")
					if(element[1] == True):
						canvas.create_oval(j * 50 + 15, k * 50 + 15, j * 50 + 35, k * 50 + 35, outline='black')
			else:
				canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="light grey", outline='light grey')
		fenetre.update()

	refresh(plateau, fenetre, canvas)

	# Ajouter une gestion d'événement pour savoir si un joueur a cliqué sur un pion
	def pion_clique(event):
		global click
		global choixDeplacement
		# Récupérer les coordonnées du clic de la souris
		x, y = event.x, event.y
		# Calculer la ligne et la colonne du pion sélectionné
		ligne = x // 50
		colonne = y // 50
		
		if(click == None):
			click = [ligne,colonne]
		else:
			lignes 	 = [6,1,7,2,8,3,9,4,10,5]
			colonnes = [0,0,10,10,20,20,30,30,40,40]
			choixDeplacement = lignes[ligne]+ colonnes[colonne]

	canvas.bind("<Button-1>", pion_clique)
	def afficheCoupJouable():
		# Afficher les coordonnées du pion sélectionné
		global coups
		ligne = click[0]
		colonne = click[1]
		if((ligne+colonne)%2 == 1 and joueur == 0):
			lignes 	 = [6,1,7,2,8,3,9,4,10,5]
			colonnes = [0,0,10,10,20,20,30,30,40,40]
			case = lignes[ligne]+colonnes[colonne]
			if(plateau[case-1] != None and plateau[case-1][0] == 0):
				deplacements = ia.getDeplacementsPossibles(plateau,case)
				# Affichage des déplacements possibles
				if(timer%2 == 1):
					canvas.create_oval(ligne * 50 + 11, colonne * 50 + 11, ligne * 50 + 39, colonne * 50 + 39, outline="#56f0e5", width=3)
				fenetre.update()
				for deplacement_type in deplacements:
					for deplacement in deplacements[deplacement_type]:
						if(deplacement not in coups):
							coups.append(deplacement)
						if(len(deplacement) == 3 and deplacement[2] != -1):
							co = getCoordonee(deplacement[2])
							k = co[1]
							j = co[0]
							canvas.create_line(j*50 +15, k*50 + 15, j*50 + 35, k*50 + 35, fill="red", width=3)
							canvas.create_line(j*50 +35, k*50 + 15, j*50 + 15, k*50 + 35, fill="red", width=3)
						if(timer%2 == 0):
							co = getCoordonee(deplacement[1])
							k = co[1]
							j = co[0]
							canvas.create_oval(j * 50 + 15, k * 50 + 15, j * 50 + 35, k * 50 + 35, fill="#56f0e5")

	def main():
		global joueur
		global choixDeplacement
		global coups
		global click
		global timer

		refresh(plateau, fenetre,canvas)
		if(joueur == 1):
			# L'IA joue
			coup = ia.play(plateau,joueur)
			if(coup == None):
				print('plu de coup')
				exit
			jouer(plateau,coup,canvas)
			joueur += 1
			joueur = joueur%2
		else:
			# Le joueur joue
			if(click != None):
				afficheCoupJouable()
				if(choixDeplacement != None):
					find = False
					for coup in coups:
						if(choixDeplacement == coup[1]):
							jouer(plateau,coup,canvas)
							click = None
							choixDeplacement = None
							coups = []
							joueur += 1
							joueur = joueur%2
							find = True
					if(find == False):
						click = None
						choixDeplacement = None
						coups = []
		timer += 1
		timer = timer%10
		fenetre.after(200,main)

	# Afficher la fenêtre
	main()
	fenetre.mainloop()
		
# Exemple d'utilisation
afficher_plateau()



# Jeu console : 
# # Création plateau
# plateau = [[0,True]] + 5*[None] + [[1,False]] + 14*[None] + [[1,True]] + 3*[None] + [[0,False]] + 24*[None]
# plateau = 50*[None]
# # plateau[32] = [1, False]
# plateau[19] = [1, False]
# plateau[24] = [0, False]
# afficher(plateau)
# # plateau = 20*[[1,False]] + 10*[None] + 20*[[0,False]]
# coup = ia.play(plateau,1)
# print('va jouer : '+str(coup))
# if(coup == None):
# 	exit
# jouer(plateau, coup)

# vainceur = None
# joueur = True
# while(vainceur == None):
# 	afficher(plateau)
# 	jouer(plateau,ia.play(plateau,joueur))
# 	if(joueur):
# 		joueur = False
# 	else:
# 		joueur = True
# 	vainceur = iSvictoire(plateau)
# 	time.sleep(5)

# print("Victoire de "+str(vainceur))
import tkinter as tk
import ia
import time

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

def jouer(plateau,coup):
	plateau[coup[1]-1] = plateau[coup[0]-1]
	plateau[coup[0]-1] = None
	
	if(coup[2] != None):
		if(coup[2] == 'dame'):
			plateau[coup[1]-1][1] = True
		else:
			plateau[coup[2]-1] = None
			
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
	# plateau = 20*[None] + 1*[[0,False]] + 1*[[1,False]] + 28*[None]
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
					canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="white")
					if(element[1]):
						canvas.create_oval(j * 50 + 15, k * 50 + 15, j * 50 + 35, k * 50 + 35, outline='black')
				else:
					canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="black")
					if(element[1]):
						canvas.create_oval(j * 50 + 15, k * 50 + 15, j * 50 + 35, k * 50 + 35, outline='white')
			else:
				canvas.create_oval(j * 50 + 10, k * 50 + 10, j * 50 + 40, k * 50 + 40, fill="light grey", outline='light grey')
		fenetre.update()
	refresh(plateau, fenetre, canvas)

	# Ajouter une gestion d'événement pour savoir si un joueur a cliqué sur un pion
	def pion_clique(event):
		# Récupérer les coordonnées du clic de la souris
		x, y = event.x, event.y
		# Calculer la ligne et la colonne du pion sélectionné
		ligne = x // 50
		colonne = y // 50
		# Afficher les coordonnées du pion sélectionné
		print(f"Pion sélectionné : ligne {ligne}, colonne {colonne}")

	canvas.bind("<Button-1>", pion_clique)

	# Afficher la fenêtre
	# fenetre.mainloop()

	vainceur = None
	joueur = True
	while(vainceur == None):
		print('tour')
		refresh(plateau, fenetre,canvas)
		jouer(plateau,ia.play(plateau,joueur))
		if(joueur):
			joueur = False
		else:
			joueur = True
		vainceur = iSvictoire(plateau)
		time.sleep(2)
		#TODO gestion du joueur (choix coup, possibilités,..)
# Exemple d'utilisation
afficher_plateau()



# Jeu console : 
	# Création plateau
	# plateau = 20*[[1,False]] + 10*[None] + 20*[[0,False]]

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
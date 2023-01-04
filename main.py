from tkinter import * 
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
		if(plateau[coup[2]-1] == 'Dame'):
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


# fenetre = Tk()

# label = Label(fenetre, text="Hello World")
# label.pack()

# fenetre.mainloop()

# Création plateau
plateau = 20*[[1,False]] + 10*[None] + 20*[[0,False]]

vainceur = None
joueur = True
while(vainceur == None):
	afficher(plateau)
	jouer(plateau,ia.play(plateau,joueur))
	if(joueur):
		joueur = False
	else:
		joueur = True
	vainceur = iSvictoire(plateau)
	time.sleep(5)

print("Victoire de "+str(vainceur))
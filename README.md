"# PS-2023-Jeu-dames-python" 

*PS = Projet Scolaire*

## 📚 Projet Scolaire | Jeu de dames en python

Janvier 2023

Groupe : Juliette, Flavien & Lucas

### 📌 Consignes du projet :
L’objectif de ce TP est de programmer une interface graphique pour le jeu de dames (en version simplifiée) entre joueurs humains ou contre l’ordinateur.

L’objectif du jeu est de retirer les pions de l’adversaire sur le damier en effectuant des “captures” ou de l’empêcher de jouer.

Damier

• Le damier est divisé en 10x10 cases.
• Chaque joueur possède 20 pions (40 en tout).
• Seules les cases noires sont utilisées (on ne pose pas les pions sur les cases blanches). Les cases noires sont donc numérotées (pour les joueurs de tournoi ou ceux qui s’exercent avec des ouvrages) de 1 à 50.
• Le camp du 1er joueur est en bas (cases 31 à 50) et celui du 2e joueur en haut (cases 1 à 20).

Pions

• Le Pion se déplace diagonalement d’une seule case vers l’avant.
• Le Pion se déplace toujours sur une case libre.
• Le Pion ne recule pas lorsqu’il se déplace.
• Lorsque le Pion atteint la dernière rangée (la dernière ligne horizontale), il devient une Dame.

Dames

• La Dame est un Pion spécial qui peut avancer, mais également reculer pour se déplacer.
• Contrairement aux règles officielles, la dame ne peut pas se déplacer de plusieurs cases dans cette version.

Captures

• Il est possible de “capturer” un pièce de l’adversaire
• Les captures, qu’elles soient exécutées par des Pions ou des Dames se font en avançant ou en
reculant : un Pion peut donc reculer en capturant une pièce (et uniquement en capturant).
• Contrairement aux règles officielles, il n’est pas obligatoire dans cette version de
capturer une pièce quand cela est possible.
• Contrairement aux règles officielles, lorsqu’une pièce (Pion ou Dame) capture et se
retrouve de nouveau en diagonal d’une pièce adverse cette pièce NE peut PAS re-capturer
au même tour (le tour s’arrête).

Conditions de victoire

• Si un joueur n’a plus de pièce, il perd la partie.
• Si un joueur ne peut déplacer aucune pièce lors d’un tour de jeu, il perd la partie.
• Si aucun joueur n’a été déclaré vainqueur après 1,000 tours de jeu par joueur (soit 2000
tours de jeu en tout), on considère que la partie est nulle.

[voir pdf]


### 💻 Applications et langages utilisés :

+ Python
+ Atom, Visual studio code



## 🌸 Merci !
© J-IFT

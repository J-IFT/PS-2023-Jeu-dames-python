from tkinter import * 
import ia

# fenetre = Tk()

# label = Label(fenetre, text="Hello World")
# label.pack()

# fenetre.mainloop()

# Création plateau
plateau = 20*[[1,False]] + 10*[None] + 20*[[0,False]]

ia.play(plateau,True)
print(plateau)

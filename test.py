import tkinter as tk

def bouton_clic(valeur):
    entree_texte.insert(tk.END, valeur)

def calculer():
    try:
        expression = entree_texte.get()
        resultat = str(eval(expression))
        entree_texte.delete(0, tk.END)
        entree_texte.insert(0, resultat)
    except Exception as e:
        entree_texte.delete(0, tk.END)
        entree_texte.insert(0, "Erreur")

def effacer():
    entree_texte.delete(0, tk.END)

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Calculatrice")

# Créer une zone de texte pour l'entrée
entree_texte = tk.Entry(fenetre, width=20)
entree_texte.grid(row=0, column=0, columnspan=4)

# Créer les boutons numériques
boutons_numeriques = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

row_num = 1
col_num = 0
for bouton in boutons_numeriques:
    tk.Button(fenetre, text=bouton, command=lambda valeur=bouton: bouton_clic(valeur)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Créer les boutons d'opérations
boutons_operations = ['+', '-', '*', '/']

row_num = 1
col_num = 4
for bouton in boutons_operations:
    tk.Button(fenetre, text=bouton, command=lambda valeur=bouton: bouton_clic(valeur)).grid(row=row_num, column=col_num)
    row_num += 1

# Bouton de calcul
tk.Button(fenetre, text="=", command=calculer).grid(row=5, column=4)

# Bouton pour effacer
tk.Button(fenetre, text="C", command=effacer).grid(row=5, column=3)

fenetre.mainloop()

import tkinter as tk
 
fenetre = tk.Tk()
fenetre.title("Ma première app")

def action_bouton():
    try:
        nombre1 = float(champ_texte1.get())
        nombre2 = float(champ_texte2.get())
        operation = champ_texte3.get()

        if operation == "+":
            resultat = nombre1 + nombre2
        elif operation == "-":
            resultat = nombre1 - nombre2
        elif operation == "*":
            resultat = nombre1 * nombre2
        elif operation == "/":
            resultat = nombre1 / nombre2
        elif operation == "**":
            resultat = nombre1 ** nombre2
        
        
        champ_texte1.delete(0, tk.END)
        champ_texte2.delete(0, tk.END)
        champ_texte3.delete(0, tk.END)
        champ_texte4.delete(0, tk.END)
        if resultat.is_integer():
            resultat_entier = int(resultat)
            champ_texte4.insert(0, str(resultat_entier))
        else:
            champ_texte4.insert(0, str(resultat))

    except:
        champ_texte1.delete(0, tk.END)
        champ_texte2.delete(0, tk.END)
        champ_texte3.delete(0, tk.END)
        champ_texte4.delete(0, tk.END)
        champ_texte4.insert(0, "Erreur")

etiquette = tk.Label(fenetre, text="Entrez le premier nombre :")
etiquette.pack()
 
champ_texte1 = tk.Entry(fenetre)
champ_texte1.pack()

etiquette = tk.Label(fenetre, text="Entrez le deuxième nombre :")
etiquette.pack()
 
champ_texte2 = tk.Entry(fenetre)
champ_texte2.pack()

etiquette = tk.Label(fenetre, text="Choisissez le type d'opération : +, -, *, /, **")
etiquette.pack()

champ_texte3 = tk.Entry(fenetre)
champ_texte3.pack()
 
etiquette = tk.Label(fenetre, text="Résultat :")
etiquette.pack()

champ_texte4 = tk.Entry(fenetre)
champ_texte4.pack()

bouton = tk.Button(fenetre, text="Cliquez pour obtenir le résultat", command=action_bouton)
bouton.pack()
 
fenetre.geometry("400x300")
fenetre.mainloop()
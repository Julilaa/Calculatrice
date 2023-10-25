import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice")

def calculer():
    try:
        # Récupère le contenu du champ de texte d'entrée et le stocke dans la variable expression
        expression = champ_texte.get()
        # La fonction eval() prend une chaîne de caractères contenant une expression mathématique (par exemple, "2 + 3 * 4") et la calcule
        resultat = str(eval(expression))
        # Efface le contenu en supprimant tous les caractères de la position 0 (le début) jusqu'à la fin (tk.END).
        champ_texte.delete(0, tk.END)
        # Insère le résultat du calcul dans le champ de texte d'entrée à la position 0, remplaçant l'expression mathématique entrée
        champ_texte.insert(0, resultat)
    except:
        # Gère les erreurs en supprimant le champ de texte et en indiquant Erreur
        champ_texte.delete(0, tk.END)
        champ_texte.insert(0, "Erreur")

def effacer():
    # Permet de supprimer le résultat de l'opération
    champ_texte.delete(0, tk.END)


etiquette = tk.Label(fenetre, text="Entrez votre calcul !")
etiquette.pack()

# Affiche le champ de texte
champ_texte = tk.Entry(fenetre)
champ_texte.pack()

# Bouton de calcul
boutton = tk.Button(fenetre, text="Calculer", command=calculer)
boutton.pack()

# Bouton pour effacer
boutton = tk.Button(fenetre, text="Effacer", command=effacer)
boutton.pack()

fenetre.geometry("400x300")
fenetre.mainloop()


# Créez votre propre interface à l'aide de Tkinter pour afficher un formulaire d'inscription comprenant un champ 
# pour le pseudo, un champ pour le mot de passe et un champ pour l'adresse e-mail. 
# Une fois l'inscription validée, les données saisies doivent s'afficher sur le terminal.

import tkinter as tk

# Récupération des informations et affichage de celles-ci dans le terminal.
def get_user_information():

    pseudo = pseudo_input.get()
    password = password_input.get()
    email = email_input.get()
    
    print("\n~~ Exercice 2 : Interface graphique ! ~~\n")
    print("L'inscription a été acceptée !\n")
    print(f"Voici les informations de l'utilisateur :\nPseudo : {pseudo}\nEmail : {email}\nMot de passe : {password}\n")


# Création de l'interface graphique.
fenetre = tk.Tk()
fenetre.title("Notre interface !")

# Création des différents titres, des entrées et du bouton.
pseudo_user = tk.Label(fenetre, text="Entrez votre pseudo : ")
email_user = tk.Label(fenetre, text="Entrez votre adresse email : ")
password_user = tk.Label(fenetre, text="Entrez votre mots de passe : ")

pseudo_input = tk.Entry(fenetre)
email_input = tk.Entry(fenetre)
password_input = tk.Entry(fenetre)

button_validation = tk.Button(fenetre, text="Valider votre inscription !", command=get_user_information)

# Affichage des différents titres et entrées.
pseudo_user.pack()
pseudo_input.pack()
email_user.pack()
email_input.pack()
password_user.pack()
password_input.pack()
button_validation.pack()

# Configuration de la fenêtre.
fenetre.geometry('400x300')
fenetre.mainloop()
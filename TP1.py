# Créer un programme qui permet à l'utilisateur de saisir et de gérer des informations personnelles telles que le nom, l'âge, la taille, la liste des fruits préférés, 
# un message de salutation personnalisé, les propriétés d'un produit, la manipulation de chaînes de caractères et l'entrée de l'utilisateur.

def print_user_information():

    fruits = []

    # Demander toutes les informations à l'utilisateur.
    name = input('Bonjour, quel est votre nom ? : ')
    first_name = input('Quel est votre prénom ? : ')
    age = input('Quel est votre âge ? : ')
    size = input('Quelle est votre taille ? : ')
    fruits_user = input('Quels sont vos fruits préférés ? (Veuillez les séparer par une virgule !) : ')

    # Traitement des informations.
    fruits = (fruits_user.split(", "))
    name_uppercase = name.upper()

    # Affichage des informations.
    print("\n ~~ Exercice 1 : Informations Personnelles ~~\n")
    print(f"Bonjour Monsieur {name_uppercase} {first_name}, vous avez {age} ans et vous mesurez {size} cm !\n")
    print(f"Vos fruits préférés sont: {' et '.join(fruits)}.\n")
    print(f"Vos informations personnelles sont : \nNom : {name}.\nPrenom : {first_name}\nAge : {age}\nTaille : {size} cm.")

print_user_information()



# Créez une calculatrice simple en Python qui permet à l'utilisateur d'effectuer des opérations de base (addition, soustraction, multiplication et division).

print("\nBonjour ! Voici les différentes opérations : \n\n1. Addition (1)\n2. Soustraction (2)\n3. Multiplication (3)\n4. Division (4)\n")

user_choice = int(input("Quelle opération souhaitez-vous ? "))

user_number1 = float(input("Entrez votre premier nombre ! : "))
user_number2 = float(input("Entrez votre deuxième nombre ! : "))

user_result = 0

match(user_choice):
    case 1:
        print("Vous avez choisi l'addition !")
        user_result = user_number1 + user_number2
        print(user_result)
    case 2:
        print("Vous avez choisi la soustraction !")
        user_result = user_number1 - user_number2
        print(user_result)
    case 3:
        print("Vous avez choisi la multiplication !")
        user_result = user_number1 * user_number2
        print(user_result)
    case 4:
        if user_number2 != 0:
            print("Vous avez choisi la division !")
            user_result = user_number1 / user_number2
            print(user_result)
        else:
            print("La division par zéro n'est pas autorisée !")
    case _:
        print("Choix invalide ! Veuillez entrer un choix valide de 1 à 4.")

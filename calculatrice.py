def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"
    
def puissance(a, b):
    return a ** b

def racine_carree(a):
    return a ** 0.5

def equation(a, b, c):
    if a != 0:
        return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    else:
        return "Erreur : Coefficient de x² nul"
    
def equation_second_degre(a, b, c):
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            return (-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)
        elif delta == 0:
            return -b / (2 * a)
        else:
            return "Pas de solution réelle"

print("Bienvenue dans la calculatrice de HectorLeNegger !")
print("Nous vous proposons les opérations suivantes qui sont disponibles pour vous, si vous souhaitez allez plus loin dans les niveaux de difficultés alors écrivez 5 pour accéder à la calculatrice avancée.")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("5. Calculatrice avancée")

choix = input("Entrez le numéro de l'opération (1/2/3/4/5) : ")

if choix == '1' or choix == '2' or choix == '3' or choix == '4':
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    
    if choix == '1':
        print(f"Le résultat de l'addition est : {addition(nombre1, nombre2)}")
    elif choix == '2':
        print(f"Le résultat de la soustraction est : {soustraction(nombre1, nombre2)}")
    elif choix == '3':
        print(f"Le résultat de la multiplication est : {multiplication(nombre1, nombre2)}")
    elif choix == '4':
        print(f"Le résultat de la division est : {division(nombre1, nombre2)}")

elif choix == '5':
    print("Vous avez choisi la calculatrice avancée.")
    print("Les opérations suivantes sont disponibles :")
    print("1. Puissance")
    print("2. Racine carrée")
    print("3. Equations")
    print("4. Equations du second degré")
    choix_avance = input("Entrez le numéro de l'opération avancée (1/2/3/4) : ")
    
    nombre1 = float(input("Entrez le premier nombre : "))
    if choix_avance == '1':
        nombre2 = float(input("Entrez la puissance : "))
        print(f"Le résultat de la puissance du nombre {nombre1} à la puissance {nombre2} est : {puissance(nombre1, nombre2)}")
    elif choix_avance == '2':
        print(f"La racine carrée de {nombre1} est : {racine_carree(nombre1)}")
    elif choix_avance == '3':
        nombre2 = float(input("Entrez le deuxième nombre : "))
        nombre3 = float(input("Entrez le troisième nombre : "))
        print(f"Les solutions de l'équation {nombre1}x² + {nombre2}x + {nombre3} sont : {equation(nombre1, nombre2, nombre3)}")
    elif choix_avance == '4':
        nombre2 = float(input("Entrez le deuxième nombre : "))
        nombre3 = float(input("Entrez le troisième nombre : "))
        print(f"Les solutions de l'équation {nombre1}x² + {nombre2}x + {nombre3} sont : {equation_second_degre(nombre1, nombre2, nombre3)}")
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")
else:
    print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")

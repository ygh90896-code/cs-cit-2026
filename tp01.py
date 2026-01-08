import random
import string

def chercher_lettre(cible):
    lettres = string.ascii_lowercase
    tentatives = 0
    car = ""

    while car != cible:
        car = random.choice(lettres)
        tentatives += 1
        print(f"Tentative {tentatives} : {car}")

    print(f"🎯 La lettre '{cible}' a été trouvée après {tentatives} tentatives")

chercher_lettre("t")

import random 
import string

letters=string.ascii_lowercase
car=""
while car!="t":
    car=random.choice(letters)
    print(f"la caractere choisie est :car")
    

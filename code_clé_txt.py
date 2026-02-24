
file=input("nom du fichier clé:")

with open(f"{file}.txt", "r") as file:
        key = file.readlines()  

p=0
key_size=len(str(key[0].strip() )) #nombre de letre que la clé a
key_char=str(key[0].strip())

def cesar(msg):
    resultat = ''
    for caractere in msg:
        resultat = resultat + chr((ord(caractere) +ord(key_char[len(resultat)% key_size] ))% 1114112) # 1114112 valeur max en unicode  
    return resultat

ask=""

while ask!= "n" :
    msg=input("msg : ")

    print(cesar(msg))
    
    ask=input("continue? (y/n) :")
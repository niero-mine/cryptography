
def cesar(msg, decalage):
    resultat = ''
    for caractere in msg:
        resultat = resultat + chr((ord(caractere) +decalage)% 1114112) # 1114112 valeur max en unicode 
    return resultat

ask=""

while ask!= "n" :
    msg=input("msg : ")
    decalage=int(input("decal : "))

    print(cesar(msg, decalage))
    print(cesar(cesar(msg, decalage), -decalage))
    
    ask=input("continue? (y/n) :")


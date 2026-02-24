
def cesar(msg, decalage):
    resultat = ''
    for caractere in msg:
        resultat = resultat + chr(ord(caractere)+decalage)
    return resultat

ask=""

while ask!= "n" :
    msg=input("msg : ")
    decalage=int(input("decal : "))

    print(cesar(msg, decalage))
    print(cesar(cesar(msg, decalage), -decalage))
    
    ask=input("continue? (y/n) :")

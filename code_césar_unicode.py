
loopback=1
def cesar(msg, decalage):
    resultat = ''
    for caractere in msg:
        resultat = resultat + chr(ord(caractere)+decalage)
    return resultat

while loopback==1:
    msg=input("msg : ")
    decalage=int(input("decal : "))

    print(cesar(msg, decalage))
    print(cesar(cesar(msg, decalage), -decalage))
    
    ask=input("continue? (y/n) :")
    if ask=="n" or ask=="N":
        loopback=0
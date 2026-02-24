
def position_lettre(lettre, type):
    return ord(lettre) - ord(type)

def nouvelle_lettre(indice, type):
    return chr(ord(type) + indice)

def cesar(message, decalage):
    resultat = ''
    for caractere in message:
        if 'A' <= caractere <= 'Z':
            indice = (position_lettre(caractere,'A') + decalage) % 26
            resultat = resultat + nouvelle_lettre(indice,'A')
        elif 'a' <= caractere <= 'z':
            indice = (position_lettre(caractere,'a') + decalage) % 26
            resultat = resultat + nouvelle_lettre(indice,'a')
        elif '0' <= caractere <= '9':
            indice = (position_lettre(caractere,'0') + decalage) % 10
            resultat = resultat + nouvelle_lettre(indice,'0')
        else:
            resultat = resultat + caractere
    return resultat

# tests
Message=input("msg:")
Decalage= int(input("decal:"))

print(cesar(Message,Decalage ))
print(cesar(cesar(Message, Decalage), -Decalage))
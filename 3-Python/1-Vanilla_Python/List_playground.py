
mois =['Janvier','Février','Mars','Avril','Mai','Juin','Juillet']
month =mois.copy()

month.sort() #va agir sur la liste, la liste va être inversée
print(month)

print(sorted(mois)) # On affiche la liste inversée, mais la liste va garder son ordre d'origine

month.reverse()
print(month)

print(reversed(mois))
print(list(reversed(mois))) # je ne sais pas pourquoi, mais contrairement à sorted, il faut mettre liste en plus.. voir 'iterator object'



<<<<<<< HEAD
print(message.capitalize())
print(message.count("un"))
print (message.endwith("message" 10,20))
print (message[12:20])
=======
>>>>>>> be4ddb01c0b6a3511e40a30bb16123edef95e152

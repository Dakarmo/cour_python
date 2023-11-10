print("Bonjour je viens de démarer mon 1er cours de python")

x = 3
y = 7

print('x + y =', x + y)
print('x - y =', x - y)
print('x / y =', x / y)
print('x // y =', x // y) # division entiere (tres utile pour les tableaux Numpy)
print('x * y =', x * y)
print('x ^ y =', x ** y) # x puissance y

# Opérations de comparaison
print('égalité :', x == y)
print('inégalité :', x != y)
print('inférieur ou égal :', x <= y)
print('supérieur ou égal :', x >= y)


def nom_de_la_fonction(argument_1, argument_2):
    restultat = argument_1 + argument_2
    return restultat

nom_de_la_fonction(3, 2)
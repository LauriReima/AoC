lista = [1,2,3,4,5,6,7]
lisab = lista.copy()
lista[1] = lista[3]

my_list = [1, 2, 3, 4, 5]

# Loopataan ja verrataan pareja
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        print(f"Verrataan: {my_list[i]} ja {my_list[j]}")
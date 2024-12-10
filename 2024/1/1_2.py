with open('data.txt', 'r') as tiedosto:
    rivit = tiedosto.readlines()

luvut1 = []
luvut2 = []
for rivi in rivit:
    row = rivi.strip('\n')
    luku1 = row.split(' ')[0]
    luku2 = row.split(' ')[-1]
    luvut1.append(int(luku1))
    luvut2.append(int(luku2))
total = 0
for i in range(len(luvut1)):
    total += luvut1[i] * luvut2.count(luvut1[i])

print(total) 
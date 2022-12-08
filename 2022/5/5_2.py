import re
import math
### 1=1, 2=5, 3=9....8=29, 9=33
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista = [[],[],[],[],[],[],[],[],[]]
ohjeet = open('input.txt', 'r')
kuvio = open('kuvio.txt', 'r')
k=kuvio.readlines()
for i in range(len(k)-2,-1,-1):
    for j in range(len(k[i])):
        if k[i][j] in abc:
            indeksi = math.floor(j/4)
            lista[indeksi].append(k[i][j])
o = ohjeet.readlines()
for i in o:
    rivi = i.split(' ')
    määrä = int(rivi[1])
    mistä = int(rivi[3])-1
    mihin = int(rivi[5])-1
    while määrä > 0:
        lista[mihin].append(lista[mistä][-1*määrä])
        lista[mistä].pop(-1*määrä)
        määrä -= 1
kapula = 0
vastaus = ''
while kapula < len(lista):
    vastaus += lista[kapula][-1]
    kapula +=1 
print(vastaus)
    
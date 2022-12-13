#vastaukset = 3257(tooLOW), 3991 

from math import sqrt

with open('input.txt') as t:
    data = t.readlines()

def etäisyys(a1,a2,b1,b2):
    if sqrt((a1-b1)**2+(a2-b2)**2) < 1.5:
        return True
    return False
s = (0,0)
tv = s[0]
to = s[1]
hv = s[0]
ho = s[1]

tLista = []
tpaikka = (tv,to)
tedel = s
for i in data:

    suunta = i[0]
    määrä = int(i[2:])  
    while määrä > 0:      
        if suunta == 'R':
            ho += 1
            hedel = (hv,ho-1)
        elif suunta == 'L':
            ho -= 1
            hedel = (hv,ho+1)
        elif suunta == 'D':
            hv -= 1
            hedel = (hv+1,ho)
        elif suunta == 'U':
            hv += 1
            hedel = (hv-1,ho)
        else:
            print('VIRHE')
        hpaikka = (hv,ho) 
        if etäisyys(hpaikka[0],hpaikka[1],tpaikka[0],tpaikka[1]):
            tpaikka = tpaikka
        else: 
            tpaikka = hedel      
        määrä -= 1
        tLista.append(tpaikka)
        print(tpaikka, hpaikka, hedel)

##tLista = list(dict.fromkeys(tLista))
print(len(set(tLista)))         

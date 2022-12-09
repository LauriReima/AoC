#vastaukset = 3257(tooLOW), 3991 

from math import sqrt


with open('test.txt') as t:
    data = t.readlines()

def etäisyys(a1,a2,b1,b2):
    return sqrt((a1-b1)**2+(a2-b2)**2)
s = (0,0)
tv = s[0]
to = s[1]
hv = s[0]
ho = s[1]

tLista = []
hpaikka = (hv,ho)
tedel = s
for i in data:
    print(hpaikka)
    suunta = i[0]
    määrä = int(i[2])  
    while määrä > 0:      
        if suunta == 'R':
            to += 1
            tedel = (tv,to-1)
        elif suunta == 'L':
            to -= 1
            tedel = (tv,to+1)
        elif suunta == 'D':
            tv -= 1
            tedel = (tv+1,to)
        elif suunta == 'U':
            tv += 1
            tedel = (tv-1,to)
        else:
            print('VIRHE')
        tpaikka = (tv,to) 
        if etäisyys(tpaikka[0],tpaikka[1],hpaikka[0],hpaikka[1]) < 1.5:
        ##if (hpaikka[0] == tpaikka[0] or hpaikka[0] -1 == tpaikka[0] or hpaikka[0] +1 == tpaikka[0]) and (hpaikka[1] == tpaikka[1] or hpaikka[1] -1 == tpaikka[1] or hpaikka[1] +1 == tpaikka[1]):
            hpaikka = hpaikka
        else: 
            hpaikka = tedel      
        määrä -= 1
        tLista.append(hpaikka)
        print(tpaikka, hpaikka, tedel)

tLista = list(dict.fromkeys(tLista))
print(len(tLista))         

def numbers_in_string(word):
    numero = {}
    jono = ''
    for i in san_num:
        if i in word:
            j = word.index(i)
            numero[j] = i
    arr =[]
    if len(numero) >0:
        for k in numero.keys():
            arr.append(k)
        arr.sort()
        if len(arr) > 0:
            jono += san_num[numero.get(arr[0])]
            jono += san_num[numero.get(arr[-1])]
        elif len(arr) == 0: 
            jono += san_num[numero.get(arr[0])]
    return jono
f = open("data2.txt", 'r')
data = f.readlines()
numerot = '1234567890'
san_num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
summa = 0
for line in range(len(data)):
    num = ''
    sana = ''
    rivi = data[line].strip()
    for j in range(len(rivi)):
        if rivi[j] not in numerot:
            sana += rivi[j]
        elif rivi[j] in numerot:       
            num += numbers_in_string(sana)
            num += rivi[j]
            sana = ''
        if j == len(rivi)-1:
            num += numbers_in_string(sana)
    if len(num) == 1:
        num = num+num
    else:
        num = num[0]+num[-1]
    summa += int(num)
    print(summa)



#52844 liian iso
#52837 liian pieni 
#  52840 oli oikein
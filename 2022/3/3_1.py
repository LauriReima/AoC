input = open('input.txt', 'r')
x = input.readlines()

aakkoset = '1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

for y in x:
    z = y.strip('\n')
    pit = len(z)
    sana = 0
    for i in range(0, int(pit/2)):
        if sana > 0:
            sana = 0
            break
        for j in range(int(pit/2), pit):
            if z[i] == z[j]:
                sum += aakkoset.find(z[i])
                sana += 1
                break
if 'nok' in aakkoset:
    print('jou')


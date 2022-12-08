input = open('input.txt', 'r')
x = input.readlines()

aakkoset = '1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
i = 0
j = 0
while i < len(x):
    
    z = x[i].strip('\n')
    pit = len(z)
    for k in z:
        if k in x[i+1] and k in x[i+2]:
            sum += aakkoset.find(k)
            break
    i += 3
print(sum)
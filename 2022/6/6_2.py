with open('input.txt') as t:
    data1 = t.read()
    data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
i = 0
while True:
    sana = ""
    for j in range(14):
        if data[i+j] not in sana:
            sana += data[i+j]
        else:
            sana = ''
            i += 1
    if len(sana) == 14:
        break
print(data.find(sana)+14)

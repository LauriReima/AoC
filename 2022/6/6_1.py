with open('input.txt') as t:
    data = t.read()
i = 0

while True:
    if data[i] != data[i+1] and data[i] != data[i+2] and data[i] != data[i+3] and data[i+1] != data[i+2] and data[i+1] != data[i+3] and data[i+2] != data[i+3]:
        print(i+4)
        print(data[i:i+4])
        break
    i += 1
print(data.find('szfm'))
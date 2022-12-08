# A = rock
# B = paper
# C = scissor

# X = rock = 1
# Y = paper = 2
# Z = scissor = 3

input = open('advent.txt', 'r')
x = input.readlines()
sum = 0
for i in x:  
    rivi = i.strip('\n')
    if rivi[0] == 'A':
        if rivi[2] == 'X':
            sum += 4
        elif rivi[2] == 'Y':
            sum += 8
        elif rivi[2] == 'Z':
            sum += 3
    elif rivi[0] == 'B':
        if rivi[2] == 'X':
            sum += 1
        elif rivi[2] == 'Y':
            sum += 5
        elif rivi[2] == 'Z':
            sum += 9
    elif rivi[0] == 'C':
        if rivi[2] == 'X':
            sum += 7
        elif rivi[2] == 'Y':
            sum += 2
        elif rivi[2] == 'Z':
            sum += 6
print(sum)

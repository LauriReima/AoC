# A = rock = 1
# B = paper = 2
# C = scissor = 3

# X = lose = 0 
# Y = tie = 3 
# Z = win = 6 

input = open('advent.txt', 'r')
x = input.readlines()
sum = 0
for i in x:  
    rivi = i.strip('\n')
    if rivi[0] == 'A':
        if rivi[2] == 'X':
            sum += 3
        elif rivi[2] == 'Y':
            sum += 4
        elif rivi[2] == 'Z':
            sum += 8
    elif rivi[0] == 'B':
        if rivi[2] == 'X':
            sum += 1
        elif rivi[2] == 'Y':
            sum += 5
        elif rivi[2] == 'Z':
            sum += 9
    elif rivi[0] == 'C':
        if rivi[2] == 'X':
            sum += 2
        elif rivi[2] == 'Y':
            sum += 6
        elif rivi[2] == 'Z':
            sum += 7
print(sum)

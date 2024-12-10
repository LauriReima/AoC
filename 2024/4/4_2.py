with open('data.txt', 'r') as tiedosto:
    lines = [line.strip() for line in tiedosto.readlines()]

def check_for_x(data, x, y):
    top_left = data[x-1][y-1]
    top_right = data[x-1][y+1]
    bottom_left = data[x+1][y-1]
    bottom_right = data[x+1][y+1]
    tl = 0
    tr = 0
    bl = 0
    br = 0
    if top_left == 'M' and bottom_right == 'S':
        tl = 1
    if bottom_left == 'M' and top_right == 'S':
        bl = 1
    if top_right == 'M' and bottom_left == 'S':
        tr = 1
    if bottom_right == 'M' and top_left == 'S':
        br = 1    
    if tl+tr+bl+br == 2:
        return 1
    return 0

xmasses = 0
num_of_lines = len(lines) 
for i in range(num_of_lines):
    num_of_rows = len(lines[i])
    for j in range(num_of_rows):
        if i > 0 and i < num_of_lines-1 and j > 0 and j < num_of_rows-1 and lines[i][j] == 'A':
            xmasses += check_for_x(lines, i, j)
print(xmasses)
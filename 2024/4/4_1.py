with open('data.txt', 'r') as tiedosto:
    lines = [line.strip() for line in tiedosto.readlines()]

def check_direction(data, x, y, x_dir, y_dir):
    if data[x][y] == 'X':
        if data[x + x_dir][y + y_dir] == 'M':
            if data[x + (2*x_dir)][y + (2*y_dir)] == 'A':
                if data[x + (3*x_dir)][y + (3*y_dir)] == 'S':
                    return 1
    return 0
xmasses = 0
num_of_lines = len(lines) 
for i in range(num_of_lines):
    num_of_rows = len(lines[i])
    for j in range(num_of_rows):
        if j <= num_of_rows - 4:
            xmasses += check_direction(lines, i, j, 0, 1)
            if i <= num_of_lines - 4:
                xmasses += check_direction(lines, i, j, 1, 1)
            if i >= 3:
                xmasses += check_direction(lines, i, j, -1, 1)
        if j >= 3:
            xmasses += check_direction(lines, i, j, 0, -1)
            if i <= num_of_lines - 4:
                xmasses += check_direction(lines, i, j, 1, -1)
            if i >= 3:
                xmasses += check_direction(lines, i, j, -1, -1)
        if i <= num_of_lines - 4:
            xmasses += check_direction(lines, i, j, 1, 0)
        if i >= 3:
            xmasses += check_direction(lines, i, j, -1, 0)
        
print(xmasses)
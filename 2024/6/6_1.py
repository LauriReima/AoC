import sys

# 5667 too high

sys.setrecursionlimit(20000)

with open('data.txt', 'r') as tiedosto:
    lines = [line.strip() for line in tiedosto.readlines()]
visited = set()

def move_up(data, row, col, step):
    visited.add((row,col))
    if row == 0:
        print(step)
        return
    elif data[row - 1][col] == '#':
        move_right(data, row, col, step)
    else:
        visited.add((row,col))
        step += 1
        move_up(data, row - 1, col, step)

def move_right(data, row, col, step):
    if col == len(data[row]) -1:
        print(step)
        return
    elif data[row][col + 1] == '#':
        move_down(data, row, col, step)
    else:
        visited.add((row,col))
        step += 1
        move_right(data, row, col + 1, step)

def move_down(data, row, col, step):
    print(row)
    if row == len(data) -1:
        print(step)
        return
    elif data[row + 1][col] == '#':
        move_left(data, row, col, step)
    else:
        visited.add((row,col))
        step += 1
        move_down(data, row + 1, col, step)

def move_left(data, row, col, step):
    if col == 0:
        print(step)
        return
    elif data[row][col - 1] == '#':
        move_up(data, row, col, step)
    else:
        visited.add((row,col))
        step += 1
        move_left(data, row, col - 1, step)

for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if lines[i][j] == '^':
            pos = (i,j)

#move_up(lines, pos[0], pos[1], 0)

if pos is not None:
    move_up(lines, pos[0], pos[1], 0)
else:
    print("Virhe: Lähtöpaikkaa (^) ei löytynyt.")
print(len(visited))
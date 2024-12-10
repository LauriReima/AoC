with open('data.txt', 'r') as tiedosto:
    lines = [line.strip() for line in tiedosto.readlines()]

for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if lines[i][j] == '^':
            pos = (i,j)

rivi = pos[0]
sarake = pos[1]
k = 0
up = True
right = False
down = False
left = False
visited = set()
visited.add((rivi,sarake))
while k < 1000000:
    if rivi == 0 or rivi == len(lines) -1:
        visited.add((rivi,sarake))
        break
    elif sarake == 0 or sarake == len(lines[0]) -1:
        visited.add((rivi,sarake))
        break
    elif up:
        if lines[rivi-1][sarake] == '#':
            up = False
            right = True
        else:
            visited.add((rivi,sarake))
            rivi -= 1
            k += 1
    elif right:
        if lines[rivi][sarake+1] == '#':
            right = False
            down = True
        else:
            visited.add((rivi,sarake))
            sarake += 1
            k += 1
    elif down:
        if lines[rivi+1][sarake] == '#':
            down = False
            left = True
        else:
            visited.add((rivi,sarake))
            rivi += 1
            k += 1
    elif left:
        if lines[rivi][sarake-1] == '#':
            left = False
            up = True
        else:
            visited.add((rivi,sarake))
            sarake -= 1
            k += 1

    print(k, rivi, sarake)
print(len(visited))
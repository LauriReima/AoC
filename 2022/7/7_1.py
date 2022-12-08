with open('input.txt') as t:
    data = t.readlines()
tree = {}
i = 0
dir = []
size = 0
while i < len(data):
    rivi = data[i].strip('\n').split(' ')
    print(dir)
    
    if rivi[0] == '$':
        if rivi[1] == 'cd':
            if rivi[2] != '..':
                if len(dir) == 0:
                    dir.append(rivi[2])
                else:
                    dir.append(dir[-1]+'/'+rivi[2])
                #size = 0
            elif rivi[2] == '..':
                dir.pop(-1)
                
                
    elif rivi[0] != 'dir':
       # size += int(rivi[0]) 
        for d in dir:
            tree[d] = tree.get(d, 0) + int(rivi[0]) 
    i += 1
    
alle = 0
for j in tree:
    if tree[j] < 100001:
        alle += tree[j]
        
print(alle)
#print(tree)
#vastaukset = 1540861, 

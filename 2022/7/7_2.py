with open('input.txt') as t:
    data = t.readlines()
tree = {}
i = 0
dir = []
size = 0
while i < len(data):
    rivi = data[i].strip('\n').split(' ')    
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
    
# koko tila = 70000000
# tarvittava = 30000000
cpu = 70000000
needed = 30000000
vastaus = tree.get('/')
for j, i in tree.items(): 
    space = cpu - tree.get('/')
    f = needed - space
    
    if i > f and i < vastaus:
        vastaus = i
    #print(j,i)      
print(vastaus)

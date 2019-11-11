import fileinput

f = open("Dracula.html", "r")
dest = open("izbicki.html", "w")

z=0
file = f.read().split(" ")
for i, word in enumerate(file):
    if 'Dracula' in file[i]:
        file[i] = file[i].replace('Dracula','<b>Izbicki</b>')
    if 'dracula' in file[i]:
        file[i] = file[i].replace('dracula','<b>izbicki</b>')
    if 'DRACULA' in file[i]:
        file[i] = file[i].replace('DRACULA','<b>IZBICKI</b>')
    if 'D&nbsp' in file[i]:
        file[i] = file[i].replace('D&nbsp','I&nbsp')
    if 'R&nbsp' in file[i]:
        file[i] = file[i].replace('R&nbsp','Z&nbsp')
    if 'A&nbsp' in file[i]:
        file[i] = file[i].replace('A&nbsp','B&nbsp')
    if 'C&nbsp' in file[i]:
        file[i] = file[i].replace('C&nbsp','I&nbsp')
    if 'U&nbsp' in file[i]:
        file[i] = file[i].replace('U&nbsp','C&nbsp')
    if 'L&nbsp' in file[i]:
        file[i] = file[i].replace('L&nbsp','K&nbsp')
    if z < 3:  
        if 'A<' in file[i]:
            file[i] = file[i].replace('A<','I<')
            z+=1
    if 'count' in file[i]:
        file[i] = '<b>professor</b>'
    if 'Count' in file[i]:
        file[i] = '<b>Professor</b>'
    if 'Bram' in file[i]:
        file[i] = file[i].replace('Bram','<b>Emily</b>')
    if 'Stoker' in file[i]:
        file[i] = file[i].replace('Stoker','<b>Bisaga</b>')

        
dest.write(" ".join(file))


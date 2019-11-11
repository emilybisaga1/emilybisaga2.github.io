import bs4
import fileinput

with open("Dracula.html") as inf:
    text = inf.read()
    item = bs4.BeautifulSoup(text, features="html.parser")

with open("izbicki.html", "w") as outf:
    outf.write(str(item))

#f1 = open("Dracula.html", 'r')
#f2 = open("izbicki.html", 'w')
#for line in f1:
 #   f2.write(line.replace('Dracula', 'Izbicki'))
 #   f2.write(line.replace('Count', 'Professor'))
#f1.close()
#f2.close()
    
#f = open("izbicki.html", "w")
#for line in f:
#    f.write(line.replace('Dracula', 'Izbicki'))
#    f.write(line.replace('Count', 'Professor'))
    
#f.close()


with fileinput.FileInput("izbicki.html", inplace=True) as file:
    for line in file:
        print(line.replace(' Dracula ', '<b> Izbicki <\b>'))
with fileinput.FileInput("izbicki.html", inplace=True) as file:
    for line in file:
        print(line.replace(' count ', '<b>professor<\b>'))
with fileinput.FileInput("izbicki.html", inplace=True) as file:
    for line in file:
        print(line.replace('Count', '<b>Professor<\b>'))


        
  #  drac_title= ['D', 'R', 'A', 'C', 'U', 'L', 'A']
  #  izb_title= ['I', 'Z', 'B', 'I', 'C', 'K', 'I']
  #  i = 0
 #   while i < 7:
  #      for line in file:
  #          print(line.replace(drac_title[i], izb_title[i]), end='')
 #           i += 1


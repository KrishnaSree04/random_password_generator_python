import random
let=[]
sym=[]
num=[]
for i in range(65,91):
    let.append(chr(i))  #append into ascii character list
for i in range(97,123):
    let.append(chr(i))  #append into ascii character list
for i in range(32,48):  
    sym.append(chr(i))  #append into ascii special character list
for i in range(91,97):
    sym.append(chr(i))  #append into ascii special character list
for i in range(123,127):
    sym.append(chr(i))
num=[1,2,3,4,5,6,7,8,9,0]  #list of numbers
k=int(input(("how many alphabets?")))
l=int(input(("how many special symbools?")))
m=int(input(("how many numbers?")))
passi=[]
for i in range(1,k+1):
    char=random.choice((let))
    passi.append(char)
for i in range(1,l+1):
    char=random.choice((sym))
    passi.append(char)
for i in range(1,m+1):
    char=random.choice((num))
    passi.append(char)
print(passi)
(random.shuffle(passi))  #shuffles the password
print(passi)
generator=""
for char in passi:
    generator=generator+str(char)  #converts list to string
print(generator)  #produces the final random generated password


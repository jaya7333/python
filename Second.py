file=open("mbox.txt","w")
print(file)

z="samba\npanipuri"
z
print(z) 
"ba\na\na"
print("ba\na\na")
print(len((z)))

z="my name is jay and   i am the ceo of the future and  no one can change my life"
print(len(z))
z=z.replace(" ","\n")
z=z.split()
print(z)
print(len(z))


file1=open("jbox.txt","r")

print(file1)

#for i in file1:
    #print(i)
    
x=0
for i in file1:
    x=x+1
print(x)

   
input1=file1.read()
y=0
for b in input1:
    y=y+1
    
print(y)

print(len(file1))


############################################################################################################################################################3
file=open("mbox-short.txt")
print(file)
for i in file:
    i=i.strip()
    if i.startswith("From"):
        print(i)
        
for i in file:
    i=i.strip()
    if not i.startswith("From"):
        continue
    print(i)


file=open("mbox-short.txt")
print(file)

for i in file:
    i=i.strip()
    if not "@uct.ac.za" in i:
        continue
    print(i)
  

  

sambhu=input("please insert the file name:   ")
try:
    fi=open(sambhu)
except:
    print("not valid input")
    exit()

count=0
for i in fi:
    if i.startswith("Subject"):
        count=count+1
    print("There are",count,"in line")
    
    
#######################################################################################################################################################################


############################################################################################3
#Exercise

name=input("enter the valid file naem")
fi=open(name)
y=0
w=0
for i in fi:
    if not "X-DSPAM-Confidence:" in i:
        continue
    else:
        i=i.strip()
        y=y+1
        print(y)
        z=i[i.find("0"):i.find("0")+6]
        z=float(z)
        print(z)
        w=w+z
print(w/y)
        
################################################################################################################3
######################################################################################################################


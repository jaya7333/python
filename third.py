###List
print([1,2,"abc","xyz"])
print([12,["Fsfsdf","SFTsegts"],5645])
print([ ])

fruit="banana"
try:
    fruit[2]="k"
except:
    print("It will not work")

list1=[1,2,3,4,5,6]
list1[1]
print(list1)
list1[1]=20
print(list1)

print(len(list1))

x=range(4)
print(x)
print(range(4))
print(x[2])

fri=["MM","tgee","srg","afsg"]
for i in range(len(fri)):
    print(fri[i])

x=[1,2,3]+[4,5,6]
print(x)
print(x[2:4])
print(dir(x))

x=list()
x.append("mama")
x.append("kaka")
x.append("ragav")
print(x)
print("kaka" in x,"ma" in x)

li=[61,614,614,11,5485,45,154,58,45,4,894,561,465,4,94,6,49,46,494,6,494]
print(li)
li.sort()
print((li))

print(max(li))
print(min(li))
print(sum(li))
print(len(li))
print((sum(li)/len(li)))


lis=list()
print(lis)
while True:
    x=input("Enter the value")
    if x=="done": ##Imp
        break
    else:
        x=float(x)
        lis.append(x) ##Imp
        print(lis)

print(lis)
print(sum(lis)/len(lis))

x="my name is  jay"
print(x.split())
y='my;name;is;jay'
print(y.split(";"))

li=open("mbox-short.txt")
print(li)
for i in li:
    i=i.strip()
    if not i.startswith("From"):
        continue
    else:
        try:
            i=i.split()
            
            print(i[2])
        except:
            continue
            
################################
fname = input("Enter file name: ")
fh = open(fname)
y=list()
for i in fh:
    i=i.strip()
 
    i=i.split()

    for j in i:
        if not j in y:
            y.append(j)
y.sort()
print(y)
        
########
fname = input("Enter file name: ")
file=open(fname)
z=0
for i in file:
    if i.startswith("From "):
        i=i.strip()
        i=i.split()
        print(i[1])
        z=z+1
print("There were",z,"lines in the file with From as the first word")
        
        
####
        
########################################################################################################################3
#Dictononiers
x=dict()
x["a"]=1
x["b"]=2
x["c"]=3
x["d"]=4

print(x)
print(x["a"])

b={"a":1,"b":2,"c":3,"d":4}
print(b["a"]+62)

########################################################
x=dict()
x["jay"]=1
x["raja"]=1
print(x)
x["jay"]=x["jay"]+1
x["raja"]=x["raja"]+1
print(x)
print("raja" in x)

###############################################3
x=["a","a","c","b","c","b","b","a","c","b","b","a","a","c"]
y=dict()
for i in x:
    if not i in y:
        y[i]=1
    else:
        y[i]=y[i]+1
print(y)
###
print(y.get("a",0))
print(y.get("g",0))

y=dict()
for i in x:
    if i in y:
        y[i]=y[i]+1
    else:
        y[i]=1
        
print(y)

####
y=dict()
for i in x:
    y[i]=y.get(i,0)+1   
print(y)

###########
i=input("Enter a line")
i=i.split()
k=dict()
for j in i:
    k[j]=k.get(j,0)+1
print(k)

print(list(k))
print(k.keys())
print(k.values())
print(k.items())

#######
#Two Iteration Variables

jjj={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
print(jjj.items())

jjj={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
iii=jjj.items()
print(iii)

for i,j in iii:
    print(i,j)

########################3
aa=input("Enter the file name")
aa=open(aa)
y=dict()

for i in aa:
    i=i.split()
    for j in i:
        y[j]=y.get(j,0)+1

print(y)
yy=y.items()
print(yy)
bi= None
big=None
for i,j in yy:
    if bi is None or j>big:
        bi=i
        big=j
print(bi,big)
        
##########################################################################
############################################################################
#Exercise 
name = input("Enter file:")
fi=open(name)
y=dict()
for i in fi:
    if i.startswith("From "):
        i=i.split()
        for j in i:
            if "@" in j:
                y[j]=y.get(j,0)+1
yy=y.items()
x=None
y=None
for i,j in yy:
    if i is None or j>y:
        x=i
        y=j
print(x,y)


############################################################3
###########################################################
#Tuples
x=(1,2,3,"abc")
print(x[3])

(A,B,C)=(1,2,3)
print(A)

print((0,1,2)<(5,1,2))
print((0,1,2)<(0,2,3))
print((1,1,2)<(0,0,3))

x=("a","z","1","d","e","0")
print(sorted(x)


##########3
y={"eg":666,"gweg":184,"ehwgt":896,"ewyt":423,"trwhytr":425,"rthr":152,"htrh":963,"trhyr":789,"hrt":425,"hgds":596}
#print(y["eg"])
y=y.items()
#print(y)
z=list()
#print(y)
for i,v in y:
    z.append((v,i))
    z=sorted(z,reverse=True)
    for a,b in z:
        #print(b,a)

########33
############3
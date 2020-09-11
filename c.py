

file=open("romeo.txt")
z=dict()
k=list()
for i in  file:
    i=i.split()
    #print(i)
    for j in i:
        z[j]=z.get(j,0)+1
z=z.items()
#print(z)

for i,j in z:
    k.append((j,i))
    k=sorted(k,reverse=True)
    
print(k[:10])
for i,j in (k[:10]):
    print(i,j)
    
#####
x={"5":1,"6":2,"4":3}

print(sorted([(j,i) for (i,j) in x.items()]))
import csv ,time
import os 
dir_path =os.path.dirname(os.path.realpath(__file__))
path=os.path.join(dir_path,'airlines.csv')
l=[]
with open(path,'r') as f:
    r=csv.reader(f)
    for row in r:
        l.append(row[1])

n=[]
for i in range(1,len(l)):
    if l[i] in n:
        pass
    else :
        n.append(l[i])
        
d={}
for i in range(0,len(n)):
    value=l.count(n[i])
    d[n[i]]=value

nd={}
k=list(d.keys())
v=list(d.values())
sor=[]

t=v[0]
for i in range(0,len(v)):
    if v[i]>t:
        t=v[i]


ti=v[0]
for i in range(0,len(v)):
    if v[i]<ti:
        ti=v[i]
        

    
    
for i in range(0,len(k)):
    nd[v[i]]=k[i]


print('OUTPUT 1')
print(d)
print('\n')
for i in nd:
    if i==t:
        print('OUTPUT 2')
        print('Name:',nd.get(t),'Count:',t)

print('\n')        
for j in nd:
    if i==ti:
        print('OUTPUT 3')
        print('Name:',nd.get(ti),'Count:',ti)
        break
   


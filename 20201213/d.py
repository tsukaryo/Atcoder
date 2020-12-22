##TLEのため提出不可


n,m=list(map(int, input().split()))
a=[0]
if(m!=0):
    a=list(map(int, input().split()))

if(m==0):
    print(1)
    
ai=sorted(a)
real=[]
dis=[ai[0]-1]
count=0
for i in range(m-1):
    dis.append(ai[i+1]-ai[i]-1)

dis.append(n-ai[m-1])


for i in range(len(dis)):
    if dis[i]!=0:
        real.append(dis[i])



for i in range(len(real)):
    if real[i]%min(real)==0:
        count=count+real[i]//min(real)
    elif real[i]%min(real)!=0:
        count=count+dis[i]//min(real)+1

if(m!=0):
    print(count)
        
        


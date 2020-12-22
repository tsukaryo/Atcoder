## 正解

n,m,t=list(map(int, input().split()))
ab=[]
max=n
for i in range(m):
    ab.append(list(map(int, input().split())))
q=0
for i in range(m):
    if(i==0):
        n=n-ab[0][0]
        if(n<=0):
            q=1
        n=n+ab[0][1]-ab[0][0]
        if(n>=max):
            n=max
    else:
        n=n-(ab[i][0]-ab[i-1][1])
        if(n<=0):
            q=1
        n=n+(ab[i][1]-ab[i][0])
        if(n>=max):
            n=max

n=n-(t-ab[m-1][1])

if(n<=0):
    q=1


if(q==1):
    print("No")
else:
    print("Yes")




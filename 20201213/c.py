## 正解

l=int(input())
au=1
for i in range(1,12):
    au=au*(l-i)
for i in range(1,12):
    au=au//(12-i)
print(int(au))

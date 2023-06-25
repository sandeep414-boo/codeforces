n=int(input())
c=0
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.pop(0)
l2.pop(0)
d={}
for i in l1:
    if i not in d:
        d[i]=1
        c+=1
for i in l2:
    if i not in d:
        d[i]=1
        c+=1

f=0
for i in range(1,n+1):
    if i not in d:
        f=1
        break
if f==1:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')

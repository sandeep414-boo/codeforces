n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(n):
        if i==j:
            pass
        else:
            if l[i][0]==l[j][1]:
                c+=1
print(c)

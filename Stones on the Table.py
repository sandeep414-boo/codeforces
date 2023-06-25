n=int(input())
st=input()
c=0
stack=[]
for i in range(n):

    if i==0:
        stack.append(st[i])
    else:
        if stack[-1]==st[i]:
            c+=1
        else:
            stack.append(st[i])

print(c)

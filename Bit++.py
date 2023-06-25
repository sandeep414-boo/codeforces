n=int(input())
c=0
for i in range(n):
    l=input()
    if l[0]=='+' or l[-1]=='+':
        c+=1
    elif l[0]=='-' or l[-1]=='-':
        c-=1
print(c)

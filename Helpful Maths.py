s=input()
c1,c2,c3=0,0,0
for i in s:
    if i=='1':
        c1+=1
    elif i=='2':
        c2+=1
    elif i=='3':
        c3+=1
res=''
for i in range(c1):
    res+='1'+'+'
for i in range(c2):
    res+='2'+'+'
for i in range(c3):
    res+='3'+'+'
print(res[:len(res)-1])

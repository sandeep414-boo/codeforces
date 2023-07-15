s1=input()
s2=input()
le=len(s1)
res=''
for i in range(le):
    if s1[i]==s2[i]:
        res+='0'
    else:
        res+='1'
print(res)

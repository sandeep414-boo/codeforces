s=input()
d={}
c=0
for i in s:
    if i not in d:
        c+=1
        d[i]=1
    else:
        pass
if c%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
    

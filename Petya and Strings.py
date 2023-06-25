s=input()
s1=s.lower()
s=input()

s2=s.lower()
f=0
for i in range(len(s1)):
    if ord(s1[i])>ord(s2[i]):
        print('1')
        f=1
        break
    elif ord(s1[i])<ord(s2[i]):
        print('-1')
        f=1
        break
    else:
        pass
if f==0:
    print('0')

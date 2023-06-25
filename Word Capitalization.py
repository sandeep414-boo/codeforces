s=input()
res=''
for i in range(len(s)):
    if ord(s[i])>96 and i==0:
        res+=chr(ord(s[i])-32)
    else:
        res+=s[i]
print(res)

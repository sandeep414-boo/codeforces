t=int(input())
for i in range(t):
    s=input().lower()
    l=['y','e','s']
    f=0
    c=0
    if len(s)==3:
        
        if s[0]=='y' and s[1]=='e' and s[2]=='s':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    
        

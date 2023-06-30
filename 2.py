n=int(input())
if n%4==0:
    print('YES')
elif n%2==0:
    if (n//2)-1 > 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

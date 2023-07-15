n=int(input())
for i in range(n):
    if i%2==0 and i+1==n:
        print('I hate it',end=' ')
    elif i%2==0 and i+1!=n:
        print('I hate that',end=' ')
    elif i%2!=0 and i+1!=n:
        print('I love that',end=' ')
    else:
        print('I love it',end=' ')
        

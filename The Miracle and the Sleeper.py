t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    if n-m<m:
        print(n-m)
    elif n==m:
        print('0')
    else:
        ma=0
        for j in range(m,n//2):
            if n%j>ma:
                ma=n%j
        print(ma)

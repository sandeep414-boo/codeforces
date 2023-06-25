t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x=sum(l1)-sum(l2)
    if x>0:
        print('Tsondu')
    elif x==0:
        print('Draw')
    else:
        print('Tenzing')

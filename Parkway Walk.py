t=int(input())
for i in range(t):
    n,e=map(int,input().split())
    a=list(map(int,input().split()))
    if sum(a)>= e:
        print(sum(a)-e)
    else:
        print(0)

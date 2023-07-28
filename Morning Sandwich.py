n=int(input())
for i in range(n):
    b,c,h=map(int,input().split())
    
    if b>(c+h):
        print((c+h)*2+1)
    else:
        print(b*2-1)
    

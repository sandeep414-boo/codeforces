c=0
for i in range(1,6):
    l=list(map(int,input().split()))
    try:
        ind=l.index(1)
        break
    except:
        continue
print(abs(i-3)+abs(ind-2))

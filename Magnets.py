n=int(input())
c=0
for i in range(n):
    mag=input()
    if i==0:
        c+=1
    else:
        if ref[-1]==mag[0]:
            c+=1
    ref=mag
print(c)
        
    

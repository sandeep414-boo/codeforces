n=int(input())
mat=[]
for i in range(n):
    l=[1]*n
    for j in range(1,n):
        if i==0:
            l[j]=1
        else:
            l[j]=mat[i-1][j]+l[j-1]
    #print(mat)
    mat.append(l)
print(mat[-1][-1])

test=int(input())
for t in range(1, test + 1):
    n=int(input())
    k=r=c=0
    mat=[]
    for _ in range(n):
        mat.append(list(map(int,input().split())))
    for i in range(n):
        k+=mat[i][i]
        x=y=0
        for j in range(n-1):
            for l in range(j+1,n):
                if mat[i][j]==mat[i][l]:
                    if x>0:
                        break
                    r+=1
                    x=1
        for j in range(n-1):
            for l in range(j+1,n):
                if mat[j][i]==mat[l][i]:
                    if y>0:
                        break
                    c+=1
                    y=1
    print('Case #',t,': ',k,' ',r,' ',c,sep='')
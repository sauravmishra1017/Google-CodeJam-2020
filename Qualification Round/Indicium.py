test = int(input())
for t in range(1, test + 1):
    n,k=[int(s) for s in input().split()]
    print('Case #',t,': ',sep='',end='')
    if not k%n:
        print('POSSIBLE')
        mat=[]
        for i in range(1, n+1):
            mat.append(i)
        pos=k//n - 1
        for i in range(n):
            temp=[]
            for j in range(n):
                if pos>=n:
                    pos=pos%n
                temp.append(mat[pos])
                pos+=1
            print(' '.join(map(str, temp)))
            pos+=n-1
    else:
        print('IMPOSSIBLE')
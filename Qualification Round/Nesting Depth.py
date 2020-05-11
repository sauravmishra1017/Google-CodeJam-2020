test=int(input())
for t in range(1, test+1):
    s=input()
    p=0
    a=''
    for c in s:
        n=int(c)
        d=n-p
        if d==0:
            a+=c
        elif d>0:
            a+=d*'('+c
        else:
            a+=(-d)*')'+c
        p=n
    if p>0:
        a+=p*')'
    print('Case #',t,': ',a,sep='')
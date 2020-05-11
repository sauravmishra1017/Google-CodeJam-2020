def assign(a):
    a.sort()
    xend=yend=0
    arr=[]
    res=''
    for start, end, pos in a:
        if start<xend and start<yend:
            return 'IMPOSSIBLE'
        if start>=xend:
            xend=end
            arr.append(('C', pos))
        else:
            yend=end
            arr.append(('J', pos))
    arr=sorted(arr,key=lambda x:x[1])
    for c in arr:
        res+=c[0]
    return res

test = int(input())
for t in range(1, test + 1):
    n=int(input())
    a=[]
    for i in range(n):
        duration=[int(s) for s in input().split()]
        duration.append(i)
        a.append(duration)
    ans = assign(a)
    print("Case #",t,': ',ans,sep='')
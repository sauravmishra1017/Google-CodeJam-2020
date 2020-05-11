test = int(input())
for t in range(1, test + 1):
    print('Case #',t,': ',sep='',end='')
    n,d = [int(s) for s in input().split()]
    s = list(map(int,input().split()))
    s.sort()
    if d==2:
        cm = 1
        for i in range(n):
            if s.count(s[i])>=2:
                cm = 0
                break
    elif d==3:
        cm = 2
        for i in range(n):
            if s.count(s[i]*2) or (s.count(s[i])==2 and s.index(s[i])<n-2):
                cm = 1
        for i in range(n-2):
            if s.count(s[i])>=3:
                cm = 0
                break
    print(cm)
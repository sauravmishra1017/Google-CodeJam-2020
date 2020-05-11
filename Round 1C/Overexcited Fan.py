test = int(input())
for t in range(1, test + 1):
    print('Case #',t,': ',sep='',end='')
    x,y,s=[st for st in input().split()]
    x = int(x)
    y = int(y)
    for time in range(0, len(s)+1):
        if time>=abs(x)+abs(y):
            print(time)
            break
        elif time==len(s):
            print("IMPOSSIBLE")
            break
        else:  
            if s[time] == 'N':
                y+=1
            elif s[time]=='S':
                y-=1
            elif s[time]=='E':
                x+=1
            elif s[time]=='W':
                x-=1
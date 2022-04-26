n=int(input("搭了幾次電梯:"))
s=[1]
ans=0
for i in range(n):
    t=int(input("樓層:"))
    if 1<=t<=10:
        s.append(t)
    else:
        print("超出範圍")
for i in range(1,n+1):
    if s[i]>s[i-1]:
        ans+=20*(s[i]-s[i-1])
    else:
        ans+=10*(s[i-1]-s[i])
print(ans,"元")
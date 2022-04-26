n=int(input("輸入整數n:"))
s=[]
number=[]
if 2<=n<=10:
    for i in range(n):
        k=int(input("猜想距離:"))
        if 1<=k<=1000:
            s.append(k)
        else:
            print("超出範圍")
else:
    print("超出範圍")
for i in range(n):
    if s[i]%(9 or 11)==0:
        ans=i
        number.append(ans)
if len(number)>0:
    for i in range(len(number)):
        print("第"+str(number[i]+1)+"個點"+str(s[number[i]]))
else:
    print("0")

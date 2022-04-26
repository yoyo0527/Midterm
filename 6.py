from inspect import trace


a=input("輸入值為:")
b=a.split(",")
b.sort()
c=sorted(b,reverse=True)
x=""
y=""
if 1<=len(b)<=7:
    for i in range(len(b)):
        x+=b[i]
        y+=c[i]
        ans=int(y)-int(x)
    print(ans)
else:
    print("超出範圍")

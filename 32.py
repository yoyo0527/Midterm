from turtle import pen


m=int(input("小明身上有幾元:"))
ans=0
if 0<=m<=100:
    n=int(input("販賣機有幾種飲料"))
    if 1<=n<=30:
        for i in range(n):
            n=int(input(""))
            if m>=n:
                ans+=1
            else:
                continue
    else:
        print("超出範圍")

else:
    print("超出範圍")
print(ans)
a=input("輸入一字元為:")
c=[]
for i in range(len(a)):
    c.append(a[i])
b=list(reversed(c))
if c==b:
    print("YES")
else:
    print("NO")
n=int(input("任教班級數量:"))
b=[]
for i in range(n):
    a=input("每班人數:")
    b.append(a)
c=sorted(b,reverse=True)
print(c[0])
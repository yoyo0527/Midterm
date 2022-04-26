n=str(input("輸入一組四位數字為:"))
a=[]
d=""
for i in range(0,4):
    a.append(int(n[i]))
    a[i]+=7
    a[i]=a[i]%10
b=a[0]
c=a[1]
a[0]=a[2]
a[2]=b
a[1]=a[3]
a[3]=c
for x in range(0,4):
    d+=str(a[x])
print("輸出加密後的數字為:",d)

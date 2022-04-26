n=input("考試次數 學生數:")
nn=n.split(" ")
a=input("每次考試所占的比率:")
aa=a.split(" ")
s=[]
sum=0
if (int(nn[0]) and int(nn[0]))<10:
    for i in range(int(nn[1])):
        b=input("")
        bb=b.split(" ")
        if len(bb)>int(nn[0]):
            break
        else:
            s.append(bb)
else:
    print("超出範圍")
for i in range(int(nn[1])):
    for y in range(int(nn[0])):
        sum+=int(s[i][y])*float(aa[y])
print("全班的總平均值為:%0.2f"%(sum/3))
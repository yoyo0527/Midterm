a=input("甲方的數字:")
b=input("乙方的數字:")
s=""
for i in range(len(a)):
    if a[i]!=b[i]:
        if a[i]=="1":
            if b[i]=="5":
                s+="贏"
            elif b[i]=="2":
                s+="輸"
            else:
                s+="和"
        elif a[i]=="2":
            if b[i]=="1":
                s+="贏"
            elif b[i]=="3":
                s+="輸"
            else:
                s+="和"
        elif a[i]=="3":
            if b[i]=="2":
                s+="贏"
            elif b[i]=="4":
                s+="輸"
            else:
                s+="和"
        elif a[i]=="4":
            if b[i]=="3":
                s+="贏"
            elif b[i]=="5":
                s+="輸"
            else:
                s+="和"
        elif a[i]=="5":
            if b[i]=="4":
                s+="贏"
            elif b[i]=="1":
                s+="輸"
            else:
                s+="和"
    else:
        s+="和"
print("洗刷刷結果:"+s)
while True:
    a=int(input("輸入第一行正整數為:"))
    b=input("第二行中數列中的數字為:")
    c=b.split(" ")
    c.sort()
    d=""
    if len(c)==a and int(c[-1])<=a:
        for i in range(len(c)):
            d+=str(c.count(c[i]))
        e=sorted(d,reverse=True)
        if e[0]=="1":
            print("每個數字剛好只出現1次")
            break
        else:
            for i in range(len(c)):
                if e[0]==d[i]:
                    c[i]
            print("最大出現次數的數字為:",c[i])
            print("出現次數為:",e[0])
            break
    else:
        continue


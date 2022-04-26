choose=input("選擇方式1 or 2:")
c={}
if choose=="1":
    n=int(input("輸入比數n:"))
    for i in range(n):
        a=input("")
        b=a.split(" ")
        c[b[0]]=int(b[1])
        print("%s牌得到%d面"%(b[0],c[b[0]]))
else:
    n=int(input("輸入比數n:"))
    for i in range(n):
        a=input("")
        b=a.split(" ")
        c[b[0]]=int(b[1])
        d=list(c.items())
    for key,value in d:
        print("%s牌得到%d面"%(key,value))

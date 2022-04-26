number=int(input("輸入筆數n:"))
s={}
for i in range(number):
    a=input("")
    b=a.split(" ")
    s[b[0]]=int(b[1])
    x=list(s.items())
for key,value in x:
    print("%s牌得到%d面"%(key,value))
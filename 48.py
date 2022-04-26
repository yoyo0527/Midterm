a=int(input("輸入筆數 n:"))
b={}
for i in range(a):
    c=input("輸入英文 中文:")
    d=c.split(" ")
    b[d[0]]=d[1]
s=input("輸入欲查詢單字:")
print(s,"中文意思為",b[s])

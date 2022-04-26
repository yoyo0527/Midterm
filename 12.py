a=input("輸入一整數序列為:")
b=a.split(" ")
s=""
for i in range(len(b)):
    s+=str(b.count(b[i]))
    if len(b)/2<int(s[i]):
        ans=b[i]
    else:
        ans="NO"
print("過半元素為:",ans)
    


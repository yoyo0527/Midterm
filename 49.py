a=input("請輸入英文句子:")
b=a.split(" ")
c=[]
for i in range(len(b)):
    c.append(b[i])
d=list(reversed(c))
print("輸出結果:",d)
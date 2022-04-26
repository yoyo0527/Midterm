a=input("輸入五張牌:")
b=a.split(" ")
sum=0
for i in range(len(b)):
    if b[i]=="A":
        b[i]=1
    elif b[i]=="J":
        b[i]=11
    if b[i]=="Q":
        b[i]=12
    if b[i]=="K":
        b[i]=13
    sum+=int(b[i])
print(sum)
n=int(input("請輸入陣列大小:"))
s=[]
big=[]
for i in range(n):
    a=input("")
    b=a.split(" ")
    s.append(b)
    for i in range(n):
        big.append(int(b[i])) 
big=sorted(big,reverse=True)
max=big[0]+big[1]+big[2]
for i in range(n):
    for x in range(n):
        if int(s[i][x])==(big[0]):
            ans1=str(i+1)
            ans2=str(x+1)
for y in range(n):
    for z in range(n):
        if int(s[y][z])==big[1]:
            ans3=str(y+1)
            ans4=str(z+1)
for g in range(n):
    for f in range(n):
        if int(s[g][f])==big[2]:
            ans5=str(g+1)
            ans6=str(f+1)
 
print("最大值為:"+str(max))
print("位置為("+ans1+","+ans2+")"+"("+ans3+","+ans4+")"+"("+ans5+","+ans6+")")

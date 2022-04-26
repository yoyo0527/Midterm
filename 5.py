m=int(input("輸入階層值M:"))
n=0
total=1
while total<m:
    n+=1
    total*=n   
print("超過M為",m,"的最小階層N值為:",n)
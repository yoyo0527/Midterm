s=[]
while True:
    a=input("請輸入事項(若已無事項，請輸入end):")
    if a=="end":
        break
    else:
        s.append(a)
for i in range(len(s)):
    print(str(i+1)+"."+s[i])
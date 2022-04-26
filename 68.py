a=input("請輸入第一組數字:")
b=input("請輸入第二組數字:")
aa=0
bb=0
if a==b:
    print("4A0B","全對")
else:
    for i in range(len(a)):
        if a[i]==b[i]:
            aa+=1
        elif a[i]!=b[i] and a.count(b[i])>0:
            bb+=1
    print(aa,"A",bb,"B","加油")
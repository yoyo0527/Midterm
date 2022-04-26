n=int(input("輸入一正整數:"))
if n%(2 or 11)==0 and n%(5 or 7)!=0:
    print(str(n)+"為新公倍數?:Yes")
else:
    print(str(n)+"為新公倍數?:No")

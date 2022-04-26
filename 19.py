number=int(input("測試的資料量:"))
for i in range(number):
    a=input("父、母、子女輸入:")
    b=a.split(" ")
    if b[0]=="O":
        if b[1]=="O" and b[2]=="O":
            print("YES")  
        elif (b[1]=="A" and b[2]=="A") or (b[1]=="A" and b[2]=="O"):
            print("YES")  
        elif (b[1]=="B" and b[2]=="B") or (b[1]=="B" and b[2]=="O"):
            print("YES")  
        elif (b[1]=="AB" and b[2]=="A") or (b[1]=="AB" and b[2]=="B"):
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif b[0]=="A":
        if (b[1]=="A" and b[2]=="A") or (b[1]=="A" and b[2]=="O"):
            print("YES")  
        elif (b[1]=="B" and b[2]=="A") or (b[1]=="B" and b[2]=="B") or (b[1]=="B" and b[2]=="O") or (b[1]=="B" and b[2]=="AB"):
            print("YES")  
        elif (b[1]=="AB" and b[2]=="A") or (b[1]=="AB" and b[2]=="B") or b[1]=="AB" and b[2]=="AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif b[0]=="B":
        if (b[1]=="B" and b[2]=="B") or (b[1]=="B" and b[2]=="O"):
            print("YES")  
        elif (b[1]=="AB" and b[2]=="A") or (b[1]=="AB" and b[2]=="B") or (b[1]=="AB" and b[2]=="AB"):
            print("YES")
        else:
            print("IMPOSSIBLE") 
    elif b[0]=="AB":
        if (b[1]=="AB" and b[2]=="A") or (b[1]=="AB" and b[2]=="B") or (b[1]=="AB" and b[2]=="AB"):
            print("YES")
        else:
            print("IMPOSSIBLE")
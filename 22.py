a=[[456,9000],[789,5000],[888,6000],[558,10000],[666,12000],[221,7000]]
n=int(input("輸入查詢組數N為:"))
for i in range(n):
    b=input("帳號 密碼:")
    c=b.split(" ")
    if c[0]=="123":
        d=0
        if c[1]!="456":
            print("error")
        else:
            print(a[d][1])
    elif c[0]=="456":
        d=1
        if c[1]!=789:
            print("error")
        else:
            print(a[d][1])
    elif c[0]=="789":
        d=2
        if c[1]!=888:
            print("error")
        else:
            print(a[d][1])
    elif c[0]=="336":
        d=3
        if c[1]!=558:
            print("error")
        else:
            print(a[d][1])
    elif c[0]=="775":
        d=4
        if c[1]!=666:
            print("error")
        else:
            print(a[d][1])
    elif c[0]=="566":
        d=5
        if c[1]!=221:
            print("error")
        else:
            print(a[d][1])
    else:
        print("error")

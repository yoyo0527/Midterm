a=input("輸入月租費形式及通話時間為:")
a1=a.split(",")
d=int(a1[1])
if a1[0]=="186":
    if d*0.09<=186:
        b=d*0.09
        print("通話費為:",round(b))
    elif d*0.09>186:
        b=d*0.09*0.8
        print("通話費為:",round(b))
elif a1[0]=="386":
    if d*0.08<=386:
        b=d*0.08
        print("通話費為:",round(b))
    elif d*0.08>386:
        b=d*0.08*0.7
        print("通話費為:",round(b))
elif a1[0]=="586":
    if d*0.07<=586:
        b=d*0.07
        print("通話費為:",round(b))
    elif d*0.07>586:
        b=d*0.07*0.6
        print("通話費為:",round(b))
elif a1[0]=="986":
    if d*0.06<=986:
        b=d*0.06
        print("通話費為:",round(b))
    elif d*0.06>986:
        b=d*0.06*0.5
        print("通話費為:",round(b))

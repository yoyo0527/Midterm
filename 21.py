data=[["Tom","DTGD"],["Cat","CSIE"],["Nana","ASIE"],["Lim","DBA"],["Won","FDD"]]
a=input("輸入查詢學號為:")
if a=="123":
    b=0
elif a=="456":
    b=1
elif a=="789":
    b=2
elif a=="321":
    b=3
elif a=="654":
    b=4
print("學生資料為:",a,data[b][0],data[b][1])
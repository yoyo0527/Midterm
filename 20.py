number=int(input("組數為:"))
for i in range(1,number+1):
    a=input("第"+ str(i) +"組:")
    b=a.split(" ")
    c=int(b[0])*250 + int(b[1])*175
    print("第",i,"組應收費用:",c)
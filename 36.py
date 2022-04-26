n=int(input(""))
a=""
b=""
c=""
for i in range(n*4):   
    aa=input("")
    a+=aa
for x in range(0,4):
    b+=a[x]
for y in range(4,8):
    c+=a[y]
if int(a[1])-int(a[0])==int(a[2])-int(a[1]):
    if int(c[1])/int(c[0])==int(c[2])/int(a[1]):
        ans=int(a[3])+int(a[1])-int(a[0])
        ans1=int(c[3])*int(c[1])//int(c[0])
        b+=str(ans)
        c+=str(ans1)
        print(b)
        print("此為等差數列")
        print(c)
        print("此為等比數列")
    else:
        ans=int(a[3])+int(a[1])-int(a[0])
        ans1=int(c[3])+int(c[1])-int(c[0])
        b+=str(ans)
        c+=str(ans1)
        print(b)
        print("此為等差數列")
        print(c)
        print("此為等差數列")
elif int(a[1])/int(a[0])==int(a[2])/int(a[1]):  
    if int(c[1])-int(c[0])==int(c[2])-int(a[1]):
        ans=int(a[3])*int(a[1])//int(a[0])
        ans1=int(c[3])+int(c[1])-int(c[0])
        b+=str(ans)        
        c+=str(ans1)
        print(b)
        print("此為等比數列")
        print(c)
        print("此為等差數列")
    else:
        ans=int(a[3])*int(a[1])//int(a[0])
        ans1=int(c[3])*int(c[1])//int(c[0])
        b+=str(ans)
        c+=str(ans1)
        print(b)
        print("此為等比數列")
        print(c)
        print("此為等比數列")

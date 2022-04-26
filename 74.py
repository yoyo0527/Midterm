ans=["red","blue","red","green"]
n=0
while True:
    n+=1
    s=""
    a=input("輸入四個顏色(中間以空白隔開):")
    b=a.split(" ")
    if ans==b:
        print("正確答案")
        break
    elif ans!=b: 
        if n>10:
            print("挑戰失敗")
            break
        elif  n<=10:
            for i in range(len(ans)):
                if ans[i]==b[i]:
                    s+="1"
                elif ans!=b[i] and ans.count(b[i])>0:
                    s+="2"
                else:
                    s+="3"
            print(s)
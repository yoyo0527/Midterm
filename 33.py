score=[]
ch=int(input("國文:"))
score.append(ch)
eng=int(input("英文:"))
score.append(eng)
ma=int(input("微積分"))
score.append(ma)
pe=int(input("體育:"))
score.append(pe)
design=int(input("程式設計:"))
score.append(design)
average=(ch+eng+ma+pe+design)/5
min=sorted(score)
max=sorted(min,reverse=True)
if 0<=ch or eng or ma or pe or design<=100:
    for i in range(len(score)):
        if max[0]==score[i]:
            ans=i
            if ans==0:
                ans="國文"
            elif ans==1:
                ans="英文"
            elif ans==2:
                ans="微積分"
            elif ans==3:
                ans="體育"
            elif ans==4:
                ans="程式設計"
    for i in range(len(score)):
        if min[0]==score[i]:
            ans1=i
            if ans1==0:
                ans1="國文"
            elif ans1==1:
                ans1="英文"
            elif ans1==2:
                ans1="微積分"
            elif ans1==3:
                ans1="體育"
            elif ans1==4:
                ans1="程式設計"
    print("平均分數:%0.2f"%(average))
    print("最高分科目:"+ans+str(max[0])+"分")
    print("最低分科目:"+ans1+str(min[0])+"分")
else:
    print("超出範圍")
degree=int(input("輸入一個度數(正整數):"))
if degree<=120:
    a=degree*2.1
    b=degree*2.1
    print("Summer months:%0.2f"%(a))
    print("Non-Summer months:%0.2f"%(b))
elif 120<degree<=330:
    a=120*2.1+(degree-120)*3.02
    b=120*2.1+(degree-120)*2.68
    print("Summer months:%0.2f"%(a))
    print("Non-Summer months:%0.2f"%(b))
elif 330<degree<=500:
    a=120*2.1+210*3.02+(degree-330)*4.39
    b=120*2.1+210*2.68+(degree-330)*3.61
    print("Summer months:%0.2f"%(a))
    print("Non-Summer months:%0.2f"%(b))
elif 500<degree<=700:
    a=120*2.1+210*3.02+170*4.39+(degree-500)*4.97
    b=120*2.1+210*2.68+170*3.61+(degree-500)*4.01
    print("Summer months:%0.2f"%(a))
    print("Non-Summer months:%0.2f"%(b))
else:
    a=120*2.1+210*3.02+170*4.39+200*4.97+(degree-700)*5.63
    b=120*2.1+210*2.68+170*3.61+200*4.01+(degree-700)*4.5
    print("Summer months:%0.2f"%(a))
    print("Non-Summer months:%0.2f"%(b))

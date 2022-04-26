while True:
    a=input("檢測的字串(end 結束):")
    if a=="end":
        print("檢測結束")
        break
    else:
        b=input("檢測的單一字元:")
        print("字元",b,"出現次數為:",a.count(b))
        continue
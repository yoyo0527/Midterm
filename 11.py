date=input("輸入月及日為:")
a=date.split(" ")
if a[0]=="01":
    if 21<=int(a[1])<=31:
        print("星座為:Aqauarius")
    elif 1<=int(a[1])<=20:
        print("星座為:Capricorn")
elif a[0]=="02":
    if 1<=int(a[1])<=18:
        print("星座為:Aqauarius")
    elif 19<=int(a[1])<=28:
        print("星座為:Pisces")
elif a[0]=="03":
    if 11<=int(a[1])<=20:
        print("星座為:Pisces")
    elif 21<=int(a[1])<=31:
        print("星座為:Aries")
elif a[0]=="04":
    if 1<=int(a[1])<=20:
        print("星座為:Aries")
    elif 21<=int(a[1])<=30:
        print("星座為:Taurus")
elif a[0]=="05":
    if 1<=int(a[1])<=21:
        print("星座為:Taurus")
    elif 22<=int(a[1])<=31:
        print("星座為:Gemini")
elif a[0]=="06":
    if 1<=int(a[1])<=21:
        print("星座為:Gemini")
    elif 22<=int(a[1])<=30:
        print("星座為:Cancer")
elif a[0]=="07":
    if 1<=int(a[1])<=22:
        print("星座為:Cancer")
    elif 23<=int(a[1])<=31:
        print("星座為:Leo")
elif a[0]=="08":
    if 1<=int(a[1])<=23:
        print("星座為:Leo")
    elif 24<=int(a[1])<=31:
        print("星座為:Virgo")
elif a[0]=="09":
    if 1<=int(a[1])<=23:
        print("星座為:Virgo")
    elif 24<=int(a[1])<=30:
        print("星座為:Libra")
elif a[0]=="10":
    if 1<=int(a[1])<=23:
        print("星座為:Libra")
    elif 24<=int(a[1])<=31:
        print("星座為:Scorpio")
elif a[0]=="11":
    if 1<=int(a[1])<=22:
        print("星座為:Scorpio")
    elif 23<=int(a[1])<=30:
        print("星座為:Sagittarius")
elif a[0]=="12":
    if 1<=int(a[1])<=21:
        print("星座為:Sagittarius")
    elif 2<=int(a[1])<=31:
        print("星座為:Capricorn")


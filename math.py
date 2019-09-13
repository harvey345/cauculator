num=float(input("請輸入數字 : "))
an=input("請輸入運算符號 : ")
num1=float(input("請輸入數字 : "))
if an=="+":
    print("算式 :\n",num,"+",num1,"=",num+num1)
if an=="-":
    print("算式 :\n",num,"-",num1,"=",num-num1)
if an=="*":
    print("算式 :\n",num,"x",num1,"=",num*num1)
if an=="/":
    print("算式 :\n",num,"/",num1,"=",num//num1,"...",num%num1)
a = float(input("enter first value: "))
b = float(input("enter second value: "))
c = input("enter action: (+ - * /): " )
if c == "+" :
    print("Result : ", a+b)
elif c == "-" :
    print("Result : ", a-b)
elif c == "*" :
    print("Result : ", a*b)
elif c == "/" :
    if b == 0 :
        print("Division by 0 is impossible")
    else:
        print("Result : ", a/b)
else:
    print("Invalid value! Choose from list (+ - * /)")


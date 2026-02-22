num1=float(input("enter the 1st number here:"))
num2=float(input("enter the second number here:"))
choice=int(input("enter the number here:1-4:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invailid number")
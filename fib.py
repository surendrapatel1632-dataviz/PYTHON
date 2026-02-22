def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter the number here:"))
if n<=0:
    print("enter the positive number")
else:
    print("enter the fibnachhi sequence:")
    for i in range(n):
        print(fibo(i))
        
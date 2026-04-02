#60°C is 140 in Fahrenheit 45°F is 7 in Celsius in python program
choice=input("enter the 'c' celsius to fahrenheit or 'f' fahrenheit to celsius:")
if choice=='c':
    celsius=float(input("enter the temp:"))
    fahrenheit=(celsius*9/5)+32
    print("fahrenheit",fahrenheit)
elif choice=='f':
    fahrenheit=float(input("enter the temp:"))
    celsius=(fahrenheit-32)*5/9
    print("celsius",celsius)
else:
    print("no celsius or no fahrenheit")
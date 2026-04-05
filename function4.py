def convert_temperature(temp,unit):
    """this function converts temprature between celsius and fahrenhieght"""
    if unit=='c':
        return temp*9/5+32
    elif unit=='f':
        return (temp-32)*5/9
    else:
        return None
print(convert_temperature(25,'c'))    
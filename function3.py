def print_details(**kwrgs):
    for keys,value in kwrgs.items():
        print(f"{keys}:{value}")
print_details(name="krish",age="32",country="india")            

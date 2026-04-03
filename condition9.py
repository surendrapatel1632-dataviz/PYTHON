# count the number even and odd 
numbers=(1,2,3,4,5,6,7,8,9)
count_even=0
count_odd=0
for x in numbers:
    if x%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("even:",count_even)
print("odd:",count_odd)            
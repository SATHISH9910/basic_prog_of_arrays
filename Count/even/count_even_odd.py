arr = [1,3,5,34,664,32,34]

even=0
odd=0

for num in arr:
    if num % 2==0:
        even= even+1
    else:
        odd=odd+1
print("even=", even)
print("odd=", odd)
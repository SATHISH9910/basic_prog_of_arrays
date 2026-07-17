arr= [30,34,346,246]

smallest=arr[0]

for num in arr:
    if num <= smallest:
        smallest=num
print("smallest number is", smallest)
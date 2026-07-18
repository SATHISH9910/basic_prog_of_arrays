
# numbers = [10, 20, 30, 40, 50]
# target = 34

# if target in numbers:
#     print("Found")
# else:
#     print("Not Found")

arr=[24,5,3345,2345,344]

largest= arr[0]    # assume largest no is 24

for num in arr:
    if  num>largest:
        largest=num
print("largest number is" ,largest)

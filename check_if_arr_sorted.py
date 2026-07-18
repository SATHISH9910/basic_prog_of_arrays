arr = [10, 20, 30, 40, 50]

sorted_array = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")
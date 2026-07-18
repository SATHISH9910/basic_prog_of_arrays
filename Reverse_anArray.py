arr=[39,49,59,69,79]
left = 0
right = len(arr) -1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)


# Time Complexity: O(n)
# Space Complexity: O(1)

# arr = [10, 20, 30, 40, 50]

# reverse_arr=[]
# for i in range(len(arr)-1,-1,-1):
#     reverse_arr.append(arr[i])
# print(reverse_arr)
##>> Time Complexity: O(n)
# # >>Space Complexity: O(n)

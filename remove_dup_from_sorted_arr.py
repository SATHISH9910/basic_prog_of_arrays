arr = [1, 1, 2, 2, 3, 4, 4, 5]
sort = [arr[0]]

for i in range (1,len(arr)):
    if arr[i]!= arr[i-1]:
        sort.append(arr[i])
print("Array after removing duplicates", sort)

# Time Complexity: O(n)
# Space Complexity: O(n) (because we create a new list)



# This solution works only if the array is sorted because duplicate values appear next to each other.
arr=[20,4,6,4,633]
largest=arr[0]
second_largest = float("-inf") #-ve infinity  > float('-inf') → smaller than every number.
float('inf')                               #→ larger than every number.#

for num in arr[1:]:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_larges=num
print("second largest" , second_largest)

                      

                      #>-inf #
#Think of it as the smallest possible value, smaller than any integer#
"""
Sort the array in a way that have zeros at the last of the array
"""


arr = [1, 0, 3, 2, 0, 4, 9, 0, 5, 0, 7]
arr.sort()
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 7, 9]

count = 0
for i in range(len(arr)):
    if arr[i] == 0:
        count += 1

arr = arr[count:] + arr[0:count]
print(arr)

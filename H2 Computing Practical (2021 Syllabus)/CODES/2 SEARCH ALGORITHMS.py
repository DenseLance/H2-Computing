from random import randint

lst = [randint(1, 100) for _ in range(10)]
lst.sort()

print("List:", lst)

def binary_search(item):
    lower = 0
    upper = len(lst) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if item < lst[mid]: # item is found on left
            upper = mid - 1
        elif item > lst[mid]: # item is found on right
            lower = mid + 1
        else:
            return mid # return index of item in lst
    return -1

for item in lst + [0]:
    print(binary_search(item))

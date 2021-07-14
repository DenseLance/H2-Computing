from random import randint

lst = [randint(1, 100) for _ in range(10)]

print("Original list:", lst)

def bubble_sort(lst):
    for _ in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

result = lst.copy()
result = bubble_sort(result)
print("Bubble sort:", result)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

result = lst.copy()
result = insertion_sort(result)
print("Insertion sort:", result)

def selection_sort(lst):
    for i in range(len(lst) - 1):
        lowest = i
        for j in range(i + 1, len(lst)):
            if lst[lowest] > lst[j]:
                lowest = j
        lst[lowest], lst[i] = lst[i], lst[lowest]
    return lst

result = lst.copy()
result = selection_sort(result)
print("Selection sort:", result)

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        lower, higher = [], []
        for item in lst[1:]:
            if item < pivot:
                lower.append(item)
            else:
                higher.append(item)
        return quick_sort(lower) + [pivot] + quick_sort(higher)

result = lst.copy()
result = quick_sort(result)
print("Quick sort:", result)

def merge_sort(lst):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        return result + left + right
                
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

result = lst.copy()
result = merge_sort(result)
print("Merge sort:", result)

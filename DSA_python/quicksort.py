def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = lst[0]
        leftlist = [i for i in lst[1:] if i <= mid]
        rightlist = [i for i in lst[1:] if i > mid]
        return quicksort(leftlist)+[mid]+quicksort(rightlist)

print(quicksort([3,5,2,4,67,33,53]))


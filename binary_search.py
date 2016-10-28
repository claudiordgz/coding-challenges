def binarySearch(alist, item):
    first, last = 0, len(alist)

    while first < last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
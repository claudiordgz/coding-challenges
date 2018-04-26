def quicksort(l):
    def partition(arr, lo, hi):
        pivot = arr[hi]
        i = lo - 1
        left, right = lo, hi
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        print(*arr)
        return i+1

    def helper(arr, lo, hi):
        if lo < hi:
            p = partition(arr, lo, hi)
            helper(arr, lo, p-1)
            helper(arr, p+1, hi)      
    
    helper(l, 0, len(l)-1)

l = [1,3,9,8,2,7,5]
print(*l)
quicksort(l)
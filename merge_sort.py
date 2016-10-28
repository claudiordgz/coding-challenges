



def merge_sort(seq):
    def merge(seq, start, mid, end):
        assert 0 <= start < mid < end <= len(seq)
        i = start
        j = mid
        temp = []
        while i < mid and j < end:
            if seq[i] <= seq[j]:
                temp.append(seq[i])
                i += 1
            else:
                temp.append(seq[j])
                j += 1
        if j == end:
            temp.extend(seq[i:mid])
        seq[start:start+len(temp)] = temp

    def _merge_sort(seq, start, end):
        if end - start < 2:
            return 0
        mid = (start + end) // 2
        _merge_sort(seq, start, mid)
        _merge_sort(seq, mid, end)
        return merge(seq, start, mid, end)
    return _merge_sort(seq, 0, len(seq))

a = [10, 9 ,8 ,7 , 6, 5, 4, 3, 2, 1]

merge_sort(a)
print(a)
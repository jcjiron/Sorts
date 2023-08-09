
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort(arr):
    if(len(arr) <= 1):
        return arr
    
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    i = 0
    
    left_half = sort(left_half)
    right_half = sort(right_half)

    return merge(left_half, right_half)



print("""Complexity O(nlog(n)) """)
print(sort([7,5,6,4,1,2,3]))
    




numbers = list(map(int, input().split()))
n, m = numbers[0], numbers[1]

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

def merge_arrays(array1, array2):
    res = []
    i, j = 0, 0
    
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
    
    # Append remaining elements
    res.extend(array1[i:])
    res.extend(array2[j:])
    
    print(*res)

merge_arrays(array1, array2)

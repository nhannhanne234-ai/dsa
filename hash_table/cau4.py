def common_elements(arr1, arr2):
    hash_table = {}
    for x in arr1:
        hash_table[x] = True
    result = []
    for x in arr2:
        if x in hash_table and x not in result:
            result.append(x)
    return result

a1 = [1, 2, 3]
a2 = [2, 3, 4]
print(common_elements(a1, a2))
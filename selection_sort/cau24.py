def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def get_k_smallest_elements(arr, k):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        min_heapify(arr, n, i)
    result = []
    current_size = n
    for _ in range(k):
        result.append(arr[0])
        arr[0] = arr[current_size - 1]
        current_size -= 1
        min_heapify(arr, current_size, 0)
    return result

if __name__ == "__main__":
    data = [45, 12, 89, 7, 23, 4, 56, 1]
    k = 3
    
    print(f"Mảng ban đầu: {data}")
    k_min = get_k_smallest_elements(data, k)
    print(f"{k} phần tử nhỏ nhất là: {k_min}")
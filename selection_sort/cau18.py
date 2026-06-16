def compare_swaps_with_bubble():
    a_selection = [3, 2, 1]
    a_bubble = [3, 2, 1]
    
    sel_swaps = 0
    n = len(a_selection)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a_selection[j] < a_selection[min_idx]:
                min_idx = j
        a_selection[i], a_selection[min_idx] = a_selection[min_idx], a_selection[i]
        sel_swaps += 1
        
    bub_swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a_bubble[j] > a_bubble[j + 1]:
                a_bubble[j], a_bubble[j + 1] = a_bubble[j + 1], a_bubble[j]
                bub_swaps += 1
                
    print(f"selection swaps = {sel_swaps}, bubble swaps = {bub_swaps}")

compare_swaps_with_bubble()
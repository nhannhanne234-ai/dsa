def min_pass(befor, after):
    n = len(befor)
    max_move_to_left = 0
    for j in range(n):
        value = befor[j]
        position_after = -1
        for i in range(n):
            if after[i] == value:
                position_after = i
                break
        left_distance = j - position_after
        
        if left_distance > max_move_to_left:
            max_move_to_left = left_distance
            
    return max_move_to_left

arr_befor = [4, 3, 2, 1]                                                            # trạng thái đầu 
arr_after = [3, 2, 1, 4]                                                            # trạng thái sau 

print(f"{min_pass(arr_befor, arr_after)} lượt")
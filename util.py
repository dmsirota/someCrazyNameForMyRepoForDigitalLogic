def num_to_str(val, num_sys = 10):
    result = format(val, {2:'b', 10:'d', 16:'x'}[num_sys])
    return result 

def get_adjance(index, arr):
    """
    get the adjance number. 
    
    Args: 
        index: for an 4-bit array, indexs are[0, 1, 2, 3]
        arr: 4-bit int array. 

    """

    result=0
    left=index - 1
    while(left >= 0 and arr[left] == arr[index]):
        left=left - 1
        result=result + 1
    
    right=index + 1
    while (right < len(arr) and arr[right] == arr[index]):
        right=right + 1
        result=result + 1

    return result

def get_code_reward(index, arr, code_digits):    
    """
    compare arr[2] and arr[3] against with code digits.
    return code digits number in arr. 

    Args:
        index: for an 4-bit array, indexs are [0, 1, 2, 3]
        arr: 4-bt int array.
        code_digits: 2-bit int array. 
    """
    
    result=0
    if index < 2:
        return result
    if arr[2] == code_digits[0]: result=result + 1    
    if arr[3] == code_digits[1]: result=result + 1
    return result

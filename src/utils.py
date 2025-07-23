

def get_last_index(stack: dict[int, list[int]]) -> int:
    
    if stack.keys():
        return list(stack.keys())[-1]
    return -1

def get_sum(a,b):
    if b > a:
        arr = list(range(a, b+1))
    else:
        arr = list(range(b, a+1))
    
    answer = 0
    
    for x in arr:
        answer += x
    
    return answer

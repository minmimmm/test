def solution(numbers):
    tot = 0
    for i in range(0, len(numbers)):
        tot += numbers[i]
        
    avg = tot/ len(numbers)
    
    return avg
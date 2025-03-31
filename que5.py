from collections import Counter

def improved_average(a, b, c, d, e):
 
    numbers = [a, b, c, d, e]
    
    
    mean = sum(numbers) / len(numbers)
    
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[len(sorted_numbers) // 2]
    
    count = Counter(numbers)
    mode = count.most_common(1)[0][0] 
    
    return mean, median, mode

mean, median, mode = improved_average(1, 2, 3, 3, 4)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

# find_max.py
def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num
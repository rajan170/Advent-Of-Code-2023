import re

filename = "Day 1/input.txt"

def func(filename):
    sum_val = 0

    with open(filename,'r') as file:
        for line in file.readlines():
            digits = re.findall(r"\d", line)

            if digits:
                val = int(f"{digits[0]}{digits[-1]}")

                sum_val += val 
    return sum_val             

print(func(filename))    
#Result = 56108
# goal of list is to make a list of 1 million numbers, then print the outcome using a for loop
# added also a sum function to sum them; combines a different exercise



numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))

for number in numbers:
    print(number)


million_sum = sum(numbers)

print(million_sum)
import random
numbers = []
sum = 0
max = 0
min = 101
for i in range(10):
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    sum += random_number
    if random_number < min:
        min = random_number
    if random_number > max:
        max = random_number
print("Numbers: ", numbers)
print("Sum: ", sum)
print("Mean: ", sum / len(numbers))
print("Max: ", max)
print("Min: ", min)

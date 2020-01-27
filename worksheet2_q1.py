# Question 1
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
for i in range(len(numbers)):
    numbers[i] *= numbers[i]
print(numbers)

# Question 2
even = []
odd = []
for i in range(1,101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even: ", even)
print("Odd: ", odd)

# Question 3
numbers = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(numbers) - 1, -1, -1):
    for j in range(len(numbers[0]) - 1, -1, -1):
        print(numbers[i][j])

# Question 4
list = []
for i in range(100):
    list.append(i)
print(list)


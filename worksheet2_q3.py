# Question 1
for i in range(9):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

# Question 2
print("Please enter a string: ")
word = input()
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])

# Question 3
print("Please enter a string: ")
word = input()
for i in range(len(word)):
    if i < 5:
        print(word[i])
    else:
        break

# Question 4
primes = []
for i in range (1,101):
    for j in range (1,i):
        if i % j == 0 and j != 1 and j != i:
            break
        elif j == i-1:
            primes.append(i)
print("Primes: ", primes)

#  Question 5
primes = []
i = 2
while len(primes) < 100:
    for j in range (1,i):
        if i % j == 0 and j != 1 and j != i:
            i+= 1
            break
        elif j == i-1:
            primes.append(i)
            i += 1
            break
print("Primes: ", primes)
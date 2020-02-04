# Question 1
import random
secret = random.randint(1,1000)
print("Guess a number: ")
guess = int(input())
guesses = 0
while (guess != secret):
    guesses += 1
    if guess < secret:
        print("Incorrect - guess bigger!")
    else:
        print("Incorrect - guess smaller!")
    guess = int(input())

print("You guessed", secret, "after", guesses, "tries!")

# Question 2
print("Enter integers, pressing enter in between, and q when you want to finish")
num = input()
sum = 0
count = 0
while(num != 'q'):
    if not num.isdigit():
        print("Please only enter integers!")
    else:
        sum += int(num)
        count += 1
    num = input()
if sum == 0:
    avg = 0
else:
    avg = sum / count
print("Sum:", sum, "Average:", avg)
    
# Question 3
while True:
    print("Hello")

# Question 4
numbers = [5,6,7,8,9]
sum = 0
n = 0
while n < len(numbers):
    sum += numbers[n]
    n += 1
print(sum)



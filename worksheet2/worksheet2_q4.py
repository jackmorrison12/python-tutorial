#  Question 1
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

# Question 2
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib (n-2)

for i in range(1,10):
    print(fib(i))

# Question 3
DICT = {"Jack" : ["20", "Brown", "Blue"], "Joe" : ["20", "Brown", "Green"]}
name = input("Please enter a name: ")
res = DICT.get(name, False)
if not res:
    print("Name not found")
else:
    print("Name: ", name)
    print("Age: ", res[0])
    print("Hair Colour: ", res[1])
    print("Eye Colour: ", res[2])

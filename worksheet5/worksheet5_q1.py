# Question 1
def hello_world():
  return "Hello World"

# Question 2
def squared_sum(numbers):
  total = 0
  for n in numbers:
    total += n*n
  return total

# Question 3
def longer(str1, str2):
  return abs(len(str2) - len(str1))

# Question 4
def remove_vowels(word):
  result = ""
  for l in word:
    if l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u':
      continue
    else:
      result += l
  return result

# Question 5
def remove_vowels_array(strings):
  return list(map(remove_vowels, strings))

# Question 6
def divisible(nums, div):
  if div == 0:
    return 0
  count = 0
  for n in nums:
    if n % div == 0 and not n == 0:
      count += 1
  return count


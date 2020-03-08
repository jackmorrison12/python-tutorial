# Question 1
def to_upper(str):
  return str.upper()

# Question 2
def swap(str):
  return str.swapcase()

# Question 3
def put_in_array(arr, var, pos):
  arr.insert(pos, var)
  return arr

# Question 4
def flip_concat(arr):
  result = ""
  arr.reverse()
  for a in arr:
    result += a
  return result

# Question 5
def alpha_array(arr):
  result = []
  for a in arr:
    result.append(a.isalpha())
  return result

# Question 6
def encrypt(str):
  nums = []
  for s in str:
    nums.append(ord(s))
  if len(nums) == 0:
    return 0
  return min(nums) + max(nums) + (sum(nums)/len(nums))

# Question 7
def letter_frequency(str):
  result = [0]*26 
  for s in str:
    if s.islower():
      result[ord(s)-ord('a')] += 1
    elif s.isupper():
      result[ord(s)-ord('A')] += 1
  return result

# Question 8
def frequency_analysis(freqs):
  answers = []
  answers.append(chr(freqs.index(max(freqs)) + ord('a')))
  answers.append(chr(freqs.index(min(freqs)) + ord('a')))
  return answers

# Question 1
def encrypt(sentence, shift):
    result = ""
    for l in sentence:
        if l.isalpha():
            num = ord(l)
            num += shift

            if l.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif l.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            result += chr(num)
        else:
            result += l
    return result


# Question 2
def decrypt(sentence, shift):
    return encrypt(sentence, -shift)

# Question 3

def better_decrypt(sentence):
    results = [0] * 26
    for i in range(0,26):
        test = decrypt(sentence, i)
        if "Hello" in test:
            results[i] += 1
        if "Hi" in test:
            results[i] += 1
        if "sh" in test:
            results[i] += 1
        if "th" in test:
            results[i] += 1
        if " a " in test:
            results[i] += 1
    if max(results) == 0:
        return "Couldn't find good decryption"
    best = results.index(max(results))
    return decrypt(sentence, best)

enc = encrypt("This is a much longer message which we want to hide from people who may want to try and see what we are writing to each other!", 3)
dec = decrypt(enc, 3)
print(enc)
print(dec)
dec2 = better_decrypt(enc)
print(dec2)
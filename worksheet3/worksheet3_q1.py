LETTER_TO_MORSE = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',  'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}
MORSE_TO_LETTER = { '.-':'A', '-...':'B','-.-.':'C', '-..':'D', '.':'E','..-.':'F', '--.':'G', '....':'H',  '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'m', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '--..--':', ', '.-.-.-':'.','..--..':'?', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')'}

# Question 1
def morse_to_letter(morse):
    try:
        return (MORSE_TO_LETTER[morse])
    except(Exception):
        return ('Error')

# Question 2
def letter_to_morse(letter):
    try:
        return (LETTER_TO_MORSE[letter])
    except(Exception):
        return ('Error')

# Question 3
def encrypt(sentence):
    result = ""
    for s in sentence:
        morse = letter_to_morse(s)
        if s == ' ':
            result = result + " "
        elif morse != 'Error':
            result = result + morse + " "
        else:
            return "Error"
    return result

# Question 4
def decrypt(sentence):
    result = ""
    cipher = ""
    if sentence == "Error":
        return "Error"
    for s in sentence:
        if s != ' ':
            i = 0
            cipher += s
        else:
            i += 1
            if i == 2:
                result += " "
            else:
                decrypt = morse_to_letter(cipher)
                if decrypt != 'Error':
                    result += morse_to_letter(cipher)
                    cipher = ""
                else:
                    return "Error"

    return result

enc = encrypt("HELLO? IS ANYONE THERE?") 
dec = decrypt(enc)
print(enc)
print(dec)
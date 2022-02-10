import nltk
from nltk.corpus import words, names
import ssl
import re
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


words_list = words.words()
names_list = names.words()

def encrypt(plain, key):
   
    encrypted_text = ''

    for ch in plain:
      
        if ch == ' ' or not ch.isalpha():
            encrypted_text = encrypted_text + ch
        elif ch.isupper():
            encrypted_char = chr((ord(ch) + key - 65) % 26 + 65)
            encrypted_text = encrypted_text + encrypted_char
            #if encrypted_char.isalpha():
        else:
            encrypted_char = chr((ord(ch) + key - 97) % 26 + 97)
            encrypted_text = encrypted_text + encrypted_char
         
    return encrypted_text
  
def decrypt(encrypted, key):
    return encrypt(encrypted, -key)


def crack(encrypted):
    cracked_text = ''
    for shift in (range(0,26)):
        cracked_text =  decrypt(encrypted, shift)
        #print(f'shift: {shift}')
        # split the string into a list of words
        words = cracked_text.split()

        num_of_words = 0
        len_of_words = len(words)
        #print("The length of words is: ", len_of_words)
        words_percentage = 0

        for word in words:
            
            if word.lower() in words_list or word in names_list:
                #print(word)
                num_of_words += 1

                words_percentage = int((num_of_words / len_of_words) * 100)
                if words_percentage > 90:
                    print(f'correct words percentage is: {words_percentage} and the correct shift is {shift}')
                    return cracked_text
    return ""


if __name__ == "__main__":
    enc1 = encrypt('THE QUICK BROWN FOX JUMPED OVER THE LAZYLY SLEEPING DOG', 15 )
    #print(enc1)
    enc1 = encrypt('It was the best of times, it was the worst of times.', 15)
    #print(enc1)
    # assert enc1 == ('ABC DEFG')

    # # enc2 = encrypt('BcDE FGHIA', 1)
    # # assert enc2 == ('890')

    # # enc3 = encrypt('1234', 28374)
    # # print(enc3)

    enc4 = decrypt('IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV', 15)
   
    assert enc4 == 'THE QUICK BROWN FOX JUMPED OVER THE LAZILY SLEEPING DOG'

    cracked = crack('IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV')
    print(f'cracked words: {cracked}')
    #print(cracked)
   
    #assert cracked == 'THE QUICK BROWN FOX JUMPED OVER THE LAZILY SLEEPING DOG'
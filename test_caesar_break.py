# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

"""
from collections import Counter
import string

message = "Ymj vznhp gwtbs ktc ozruji tajw ymj qfed itl" 

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    if freq > maxFreq and letter != ' ':
        maxLetter = letter
        maxFreq = freq

    """maxLetter = letter_counts.most_common(3)[2][0]"""
print("Max Ocurring Letter:", maxLetter)

#predict shift

#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = letters.find(maxLetter) - 4
keys = {}
invkeys = {}
for index, letter in enumerate(letters):
    # cypher setup
    if index < 26: #lowercase
        keys[letter] = chr((ord(letter) + shift-97)%26+97)
        invkeys = {y:x for x,y in keys.items()}
        
    else: #uppercase
        keys[letter] = chr((ord(letter) + shift-65)%26+65)
        invkeys = {y:x for x,y in keys.items()}


print("Predicted Shift:", shift)

decryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage))

# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog" #type your message here
print("Message:", message)

#create the Caesar cypher
offset = 5 #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        keys[letter] = chr((ord(letter) + offset-97)%26+97)
        invkeys = {y:x for x,y in keys.items()}
        
    else: #uppercase
        keys[letter] = chr((ord(letter) + offset-65)%26+65)
        invkeys = {y:x for x,y in keys.items()}
print("Cypher Dict:", keys)

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(str(keys[letter]))
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string

#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string

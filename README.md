# Codebreaking-
Programs based on the Codebreaking lab items, that is, simple Caesar cipher and pre-built simulator of an Enigma code machine.


## `test_caesar.py`
Program that uses Python dictionaries to create a shifted directory of letters that will map input letters to shifted ones. This can be used to encrypt and decrypt the code Caesar cipher messages provided in the file. 

## `test_caesar_break.py`
Program that breaks the code and decrypt the message provided. The written algorithm assumes that particular English language such as the letter 'e' occurs more often than others.
Works with unknown shifts.

## `test_enigma_simple.py`
A working Enigma machine with access to only rotors I, II, III. Algorithm encrypts and decrypts messages.
Requires supplied file `enigma.py` and `rotor.py` to execute.

## `test_enigma_break.py`
A working Enigma machine with access to only rotors I, II, III. Algorithm breaks code through brute force, given a specified code and crib. Also returns the number of steps processed to break code.
Requires supplied file `enigma.py` and `rotor.py` to execute.

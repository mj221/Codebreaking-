# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

"""
import string
import enigma
import rotor

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ""
print(crib_substring)

##Break the code via brute force search

cracked = False
decrypt = ""
count = 0
for a in capitalLetters:
    for b in capitalLetters:
        for c in capitalLetters:
            if cracked == True:
                break
            else:
                key = a+b+c

                engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key,
                                plugs="AA BB CC DD EE")
        
                decrypt = engine.encipher(ShakesHorribleMessage)
                count+=1
                if decrypt[-12:] == crib:
                    cracked = True


#Print the Decoded message

print("Decrypted message:", decrypt)
print("Number of tries:", count)

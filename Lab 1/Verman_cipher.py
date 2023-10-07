import random as r

plain_text = input("Enter the plain text: ").replace(' ', '').upper()

key =  [(r.randint(0, 25)) for _ in range(len(plain_text))]
alphabets = [ord(char)-ord('A') for char in plain_text]

print(alphabets)

#Cipher
ciphertext = ''
for char, k in zip(alphabets, key):
    ciphertext = ciphertext + (chr(65+(char+k)%26))

print("Ciphered Text: " + ciphertext)

#Decipher
deciphertext = ''
alphabets = [ord(letter)-ord('A') for letter in ciphertext] #Converting the ciphered text to their corresponding numeral

for char, k in zip(alphabets, key):
    deciphertext = deciphertext + (chr(65+(char-k)%26))

print("Deciphered Text: " + deciphertext)
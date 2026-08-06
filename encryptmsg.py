import random
import string

symbols = " " + string.punctuation + string.digits + string.ascii_letters 

chars = list(symbols)

# print(chars)

keys =list(symbols)
random.shuffle(keys)

# print(keys)

#Encrypting a message


while True:
     normal_message = input("Enter a message to be encrypted : ")
     encrypted_message = ""

     for letter in normal_message:
         x = chars.index(letter)
         y = keys[x]

         encrypted_message += y

     print(f"Normal message : {normal_message}")
     print(f"Encrypted message : {encrypted_message}")
     print()

     again = input("Would you like to encrypt another message(y/n) : ").lower()
     if again != "y" :
         break



def decrypt():
    #Decrypting a message
    while True:
         to_be_decrypted = input("Enter a message to be decrypted : ")
         decrypted_message = ""
        
         for symbol in to_be_decrypted:
             a = keys.index(symbol)
             b = chars[a]
        
             decrypted_message += b
        
         print(f"Message to be decrypted : {to_be_decrypted}")
         print(f"Decrypted message : {decrypted_message}")
         repeat = input("Would you like to decrypt another message(y/n) : ").lower()
         if repeat != "y" :
              print("Good Bye!")
              break

     

decr = input("Would you like to decrypt a message (y/n) : ").lower()

if decr == "y":
    decrypt()
else:
    print("Good Bye!")
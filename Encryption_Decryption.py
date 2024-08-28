import random 
import string 

chracters = string.ascii_letters + string.digits + string.punctuation + " " ## include all string ASCII letters, special chracters and number 

chracters = list(chracters) ## put the options we have in a list format 
keys = chracters.copy() ## make a copy of our original characters 

random.shuffle(keys) ## shuffle the characters in our copy everytime we rerun the program


def get_user_message():# get the user message that to be encrypted
    original_text = input("Enter the message you want to encrypt: ").strip()
    return original_text

def encrypt(original_message): # function to encrypt the message 
    cipher_list = ""    # empty string that will hold the encrypted message 

    for char in original_message: ## iterate over the whole input message and replace each charcter with one from the encrypted list we made
        index = chracters.index(char) # find the index of every character 
        cipher_list += keys[index] # assign that index to keys and concatenate every time to form the encrypted text

    return cipher_list 


def decrypt(cipher_text): # function to decrypt the message to its original 
    original_message = "" # empty string to hold the result of decryption

    for char in cipher_text:
        index = keys.index(char)
        original_message += chracters[index]      

    return original_message


def main():
    user_message = get_user_message() # get the message to be encrypted from user
    encrypted_message = encrypt(user_message) # encrypt the user message
    print(f"Encrypted Message: {encrypted_message} ") # print the encrypted message on the screen
    original_message = decrypt(encrypted_message) # decrypt the encrypted message in other words return the original message (the user input)
    print(f"Message After Decryption: {original_message} ")


if __name__ == "__main__":
    main()
 

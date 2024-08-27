import random 
import string

def get_length(): ## gets the length of the password from the user
    while True:
     try:
        length = int(input("Enter The Desired Length: ").strip()) ## turn the input number from string to integer 

        if length < 1: ## handling if the user entered an invalid numberimport random 
import string

def get_length(): ## gets the length of the password from the user
    while True:
     try:
        length = int(input("Enter The Desired Length: ").strip()) ## turn the input number from string to integer 

        if length < 1: ## handling if the user entered an invalid number
            print("Invaild Length!, Length should be a postive integer")
            continue

        return length
     
     except ValueError: ## handling if the user entered anything but integer 
        print("Enter A Valid Number")



def generate_password(length):

    password = "" ## An empty string to recieve the outcome password result
    letters = string.ascii_letters  ## All uppercase,lowercase ASCII characters 

    i = 0 ## conuter initilization
    while i < length: ## While Loop to generate the password in a random fashion 

        password += random.choice(letters) ## concatenate the password characters together to generate the password
        i += 1 ## increment the counter 
    
    return password


def main():
   while True:
    password_len = get_length()
    Generated_PassWord = generate_password(password_len)
    print(f"Generated Password: {Generated_PassWord}")
    try_another = input("Enter 1 if you want to try another password otherwise,enter anything: ")
    if try_another != "1":
       print("GoodBye!")
       break


if __name__ == "__main__":
    main()    



            print("Invaild Length!, Length should be a postive integer")
            continue

        return length
     
     except ValueError: ## handling if the user entered anything but integer 
        print("Enter A Valid Number")



def generate_password(length):

    password = ""  ## An empty string to recieve the outcome password result
    letters = string.ascii_letters  ## All uppercase,lowercase ASCII characters 

    i = 0 ## conuter initilization
    while i < length: ## While Loop to generate the password in a random fashion 

        password += random.choice(letters) ## concatenate the password characters together to generate the password
        i += 1 ## increment the counter 
    
    return password


def main():
   while True:
    password_len = get_length()
    Generated_PassWord = generate_password(password_len)
    print(f"Generated Password: {Generated_PassWord}")
       
    try_another = input("Enter 1 if you want to try another password otherwise,enter anything: ")
    if try_another != "1":
       print("GoodBye!")
       break


if __name__ == "__main__":
    main()    

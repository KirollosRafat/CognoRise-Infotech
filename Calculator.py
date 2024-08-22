##This is a simple calculator## 

##Various Opertaions
def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error!,Divison By Zero Is Not Acceptable" 
    
    


def calculate(number1,number2,operation):
        #create a dicitonary of opeartions to map various operations
    operations = {
            "add" : addition,
            "subtract" : subtract,
            "multiply" : multiply,
            "divide"   : divide 
    }
    
    function = operations.get(operation) # based on opeartion chosen from the user we select the right function to it

    if function:
        return function(number1,number2)
    else:
        "Invalid"


def main():
    print("Welcome to our simple calculator.")## Welcome message

    while True:
        try:
            ## gets from the user the two numbers and the operation required 
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose one of the these operations: add, subtract, multiply, divide: ")

            result_outcome = calculate(num1,num2,operation) # performing the calculation

            print(f"The Result Is : {result_outcome}")# Displaying The calculation

            try_again = input("Do you want another operation:(Y/N): ").strip() #asks the user for another operation 

            if try_again == "N": 
                print("Program Terminated")
                break

        except ValueError:
            print("Bad Input, Enter Numeric Values Only:")       


# Run the main function
if __name__ == "__main__":
        main()    
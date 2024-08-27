import random 

def get_sides():
    return int(input("How many sides per die you want?: ").strip())
 

def get_dice():
    return int(input("Enter how many dice you prefer: ").strip())


def generate_die(sides):
    return random.randint(1,sides)

def generate_rolls(dice,sides):
    roll = 0 
    while roll < dice:
        print(f"The roll number {roll + 1} is : {generate_die(sides)}")
        roll += 1

def main():
    while True:
        try:
          die_sides = get_sides()
          if die_sides <= 0:
            print("Wrong Value:You are supposed to enter a postive integer for sides") 
            continue

          dice_number = get_dice()
          if dice_number <= 0:
              print("Wrong Value: You are supposed to enter a postive integer for dice")  
              continue 
                  
          generate_rolls(dice_number,die_sides)
          
          try_again = input("Want to go for another trial (y/n): ").lower()
          if try_again != "y": 
              print("That\'s the end of our program!")
              break
        except ValueError:
            print("NO texts are allowed, try postive intger numeric values only!")  


if __name__ == "__main__":
    main()
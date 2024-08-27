import random


game = ["rock","paper","scissors"] # Game Options


def comp_choice():
    return random.choice(game) # computer's choice



def determine_winner(user_choice, comp_choice):# Determine the winner through the game logic
   if user_choice == "rock":
    match(comp_choice):
     case "rock" : 
      return "Tie"
     case "paper": 
      return "Lose"
     case "scissors": 
      return "Win"
     

   if user_choice == "paper":
    match(comp_choice):
      case "rock" : 
         return "Win"
      case "paper": 
         return "Tie"
      case "scissors": 
         return "Lose"
         

   if user_choice == "scissors":
    match(comp_choice):
      case "rock" : 
         return "Lose"
      case "paper": 
         return "Win"
      case "scissors": 
         return "Tie"



def update_user_score(result,user_score): # If the user wins increment its score by one
    if result == "Win":
        user_score += 1
        return user_score        
    else:
        return user_score


def update_computer_score(result,computer_score): # If the computer wins increment its score
  if result == "Lose":
    computer_score += 1
    return computer_score
  else: 
    return computer_score
      

def main():
    user_score = 0
    computer_score = 0
    while True:   
        try:
         ## Players (computer and user) choices
         user_choice = input(f"pick from {game}: ") # User Choice

         if user_choice not in game: 
           print("You have to pick from rock , paper or scissors only!!")
           continue
           
                  
         computer_choice = comp_choice() # Computer Choice 
         print(f"The Computer Picked {computer_choice}") # Print The Computer Choice

         ## Who's The Winner: 
         result = determine_winner(user_choice,computer_choice) # Winner Determination 
         print(f"You {result}") # Print the Result

         ## Score Determination and Keep The Scoreboard
         computer_score = update_computer_score(result,computer_score) #Update Computer Score 
         user_score = update_user_score(result,user_score) #Update User Score
         print(f"The Scoreboard: Computer {computer_score} - User {user_score}") # Scoreboard 

         ## Another Round ?:
         another_round = input("If you want another round Write 'Y' otherwise, write anything: ").lower()
         if another_round != "y":
           print("This The End Of Our Program !")
           print(f"The Final Score: Computer {computer_score} - User {user_score}")
           break

        except Exception:
          print("Something Went Wrong") 


if __name__ == "__main__":
    main()
    

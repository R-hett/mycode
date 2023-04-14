#!/usr/bin/python3

import random

#propts user for choice selection
def get_player_choice():
    while True:
        choice = input("Choose rock (R), paper (P), or scissors (S): ").upper()
        if choice in ['R', 'P', 'S']:
            return choice
        else:
            print("Invalid choice. Try again.")

# gets random choice for computer
def get_computer_choice():
    choices = ['R', 'P', 'S']
    return random.choice(choices)


# determines winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'r' and computer_choice == 's') or\
         (player_choice == 'p' and computer_choice == 'r') or\
         (player_choice == 's' and computer_choice == 'p'):
        return "player"
    else:
        return "computer"

def main():

   # Starting score board
   user_score = 0
   comp_score = 0
   tie = 0

   player_name = input("What is your name? ").capitalize()
   # multi round loop
   while True:
      print("Let's play Rock-Paper-Scissors!")
      player_choice = get_player_choice()
      computer_choice = get_computer_choice()
      winner = determine_winner(player_choice, computer_choice)
      print(f"You chose {player_choice}, computer chose {computer_choice}.")
      if winner == "tie":
         tie += 1
         print("It's a tie!")
      elif winner == "player":
         user_score += 1
         print("You won!")
      else:
         comp_score += 1
         print("Computer wins.")


      #asks user if they wish to play again. shows scores if no
      while True:
          new_round = input("Would you like to play again? (Y)es or (N)o: ")
          if new_round.lower() in ["y","yes"]:
              print("Fantastic!")
              break
          elif new_round.lower() in ["n","no"]:
              print(f"Final scores: {player_name}-{user_score}, Computer-{comp_score}, Ties-{tie}. ")
              return
          else:
              print("Invalid input. Lets try that again. (I belive in you)" )


if __name__ == "__main__":
    main()


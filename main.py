import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

elements = [rock, paper, scissors]

player_select = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
if player_select > len(elements) - 1:
  print("That's an invalid choice. You lose.") 
else:
  print(elements[player_select])
  
  #Computer's selection
  print("Computer chose:")
  computer_selection = random.choice(elements)
  print(computer_selection)
  
  if computer_selection == elements[player_select]:
    print("It's a draw!")
  elif computer_selection == elements[0] and elements[player_select] == elements[1]:
    print("You won!")
  elif computer_selection == elements[1] and elements[player_select] == elements[2]:
    print("You won!")
  elif computer_selection == elements[2] and elements[player_select] == elements[0]:
    print("You won!")
  else:
    print("Computer won!")
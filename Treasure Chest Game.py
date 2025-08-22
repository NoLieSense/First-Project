import random


def chests():
  options = ["golden chest", "silver chest", "bronze chest"]
  computer_choice = random.choice(options)
  return computer_choice


secret = chests()

if secret == "golden chest":
  print("HINT: Chosen chest is the heaviest")
elif secret == "silver chest":
  print("HINT: Chosen chest is lightest")
if secret == "bronze chest":
  print("HINT: Chosen chest is associated with the 3rd Position")

player_choice = input(
    "Choose a chest, golden chest, silver chest, or bronze chest: ")

if player_choice == "golden":
  player_choice = "golden chest"
elif player_choice == "silver":
  player_choice = "silver chest"
elif player_choice == "golden":
  player_choice = "bronze chest"

if secret == player_choice:
  print("You win!")
else:
  print("You lose!")

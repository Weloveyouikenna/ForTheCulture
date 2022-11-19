from random import choice 
items = ["rock", "paper", "scissors"]
computer = choice(items)
rps = input("What will you choose? rock, paper, or scissors?" "\n:").lower().strip()
if rps == computer: 
  print("It is a tie :/")
if rps == ("rock"):
  if computer == ("scissors"):
    print("Yay! You won! :)")
if rps == ("paper"):
  if computer == ("rock"):
    print("Yay! You won! :)")
if rps == ("scissors"):
  if computer == ("paper"):
    print("Yay! You won! :)")
if computer == ("scissors"):
  if rps == ("paper"):
    print("Noooo!! You lost :(")
if computer == ("paper"):
  if rps == ("rock"): 
    print("Noooo!! You lost :(")
if computer == ("rock"):
  if rps == ("scissors"):
    print("Noooo!! You lost :(")
print("Thanks for playing!")

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

print(f"Pssst, the correct answer is {number}")

def guessing():

  user_guess = int(input("Make a guess: "))
  if user_guess > number:
    print("Too high.")
  elif user_guess < number:
    print("Too low.")
  else:
    print(f"You got it. The answer was {user_guess}")


attempts = 10
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
  attempts = 5

  game_is_finished = False

while not game_is_finished and attempts > 0:
  print(f"You have {attempts} remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  if user_guess > number:
    print("Too high.")
  elif user_guess < number:
    print("Too low.")
  else:
    print(f"You got it. The answer was {user_guess}")
    game_is_finished = True
  attempts -= 1
  

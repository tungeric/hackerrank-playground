###########################
## ---- Simple Game --- ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you


def check_guess(guess, secret):
  if guess != 'quit':
    i = 0
    match_count = 0
    close_count = 0
    while i < len(secret):
      guess_char = int(guess[i])
      if guess_char in secret:
        if guess_char == secret[i]:
          match_count += 1
        else:
          close_count += 1
      i += 1
    print(f"You have {match_count} direct matches.")
    print(f"You have {close_count} close matches.")
    if match_count == 3:
      return True
    else:
      return False


import random

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
digits = list(range(10))
random.shuffle(digits)
secret = digits[:3]
print("The code has been generated. Take a guess!")
guess_count = 0
guess = ""
is_correct = False
while guess != secret and is_correct == False:
  if guess == "quit":
    print("You were so close why did you quit?!")
    break
  guess = input(
      "What is your guess? (Type a 3 digit number or 'quit' to quit) ")
  is_correct = check_guess(guess, secret)
  guess_count += 1
if is_correct:
  print(
      f"CONGRATULATIONS! You guessed the secret number in {guess_count} tries.")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

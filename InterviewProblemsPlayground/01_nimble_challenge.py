# It must contain at least one vowel.
# It cannot contain three consecutive vowels or three consecutive consonants.
# It cannot contain two consecutive occurrences of the same letter, except for 'ee' or 'oo'.


def check_passwords(filepath, output_filepath):
  input = open(filepath, 'r')
  passwords = input.read().split('\n')[:-2]
  # print(passwords)
  output = open(output_filepath, 'w')
  for password in passwords:
    valid_password = is_password_valid(password)
    if(valid_password == True):
      output.write(f"<{password}> is acceptable.\n")
    else:
      output.write(f"<{password}> is not acceptable.\n")
  input.close()
  output.close()


def is_password_valid(password):
  has_vowel = False
  prev_char_is_vowel = True
  # initialize as vowel, but since count is 0 this does not impact results
  curr_char_type_count = 0
  curr_char = ''
  for char in password:
    if is_vowel(char):
      has_vowel = True
      if prev_char_is_vowel:
        curr_char_type_count += 1
      else:
        prev_char_is_vowel = True
        curr_char_type_count = 1
    else:
      if prev_char_is_vowel:
        prev_char_is_vowel = False
        curr_char_type_count = 1
      else:
        curr_char_type_count += 1
    if curr_char_type_count >= 3:
      return False
    if char == curr_char and not (char == 'e' or char == 'o'):
      return False
    curr_char = char
  return has_vowel


def is_vowel(char):
  VOWELS = ['a', 'e', 'i', 'o', 'u']
  if char in VOWELS:
    return True
  return False


## INSTRUCTIONS TO RUN


# once the file is saved:
# in terminal, use command `python solution_eric_tung.py`
# below, enter `check_passwords(filepath, output_filepath)`
# where filepath is the file directory and name of your input file as a string, and
# output_filepath is the file name of your output file as a string.
# example: check_passwords('/Users/eric-mbp/Projects/interview projects/challenge_2hours/say.in', 'solution.txt')


check_passwords('/Users/eric-mbp/Projects/interview projects/challenge_2hours/say.in', 'solution.txt')

# the program will create a file with the output file name you provided in the root directory
# containing results that match the `say.out` file provided in the problem prompt.
# If the file already exists, it will overwrite the existing contents of the file!

# Thank you for your time and consideration! Once again I am excited for this opportunity!

# list with all your letters (fill in)
answer = ["s", "t", "a", "r", "s"]
#list with whether or not each letter has been guessed
guessed = [False, False, False, False, False]


#this is a method that returns the correct image for pull up man based on however many letters have been guessed.
def ascii(correct):
  if correct == 1:
    print("__________")
    print()
    print()
    print("    O ")
    print("  / | \ ")
    print(" /  |  \ ")
    print("   / \    ")
    print("  /   \ ")
  elif correct == 2:
    print("__________")
    print()
    print(" |     |")
    print("  \ O / ")
    print("    |   ")
    print("    |    ")
    print("   / \    ")
    print("  /   \ ")
  elif correct == 3:
    print("__________")
    print(" |     |")
    print("  \ O / ")
    print("    |   ")
    print("    |    ")
    print("   / \    ")
    print("  /   \ ")
  elif correct == 4:
    print("__________")
    print("  |_O_|")
    print("    |   ")
    print("    |    ")
    print("   / \    ")
    print("  /   \ ") 
  elif correct == 5:
    print("   _ O _")
    print("__|__|__|_")
    print("     |   ")
    print("     |    ")
    print("    / \    ")
    print("   /   \ ")
  else:
    print()


def blanks():
  print("TO DO: Create a method that prints out an underscore if the letter has not been guessed and the letter if it has been guessed for each letter in the word")


def guess(letter):
 print("TO DO: congradulate the user if the letter is in the word, show them pull up man and the new blanks, and ask them to guess again, otherwise just say they didn't get the letter and have them guess again")






# gets the number of trues in the guessed list
def getCorrect():
  print("returns the number of letters that have been guessed using the guessed list")
  

  


def play():
  print("asks the user if they want to play and takes their first guess")
  


play()

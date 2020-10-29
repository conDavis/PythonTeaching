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
  result = ""
  for x in range(len(guessed)):
    if guessed[x] == True:
      result = result + answer[x] + " "
    else: 
      result = result + "_ "
  print(result)


def guess(letter):
  if letter in answer:
    for x in range(len(answer)):
      if answer[x] == letter:
        guessed[x] = True
    ascii(getCorrect())
    blanks()
    if getCorrect() == 5:
      print("YAY! You helped Pull-Up Man complete a Pull-Up! Epic! :-)")
      playAgain = input("Would you like to play again? ")
      if playAgain == "yes":
        for x in range(len(guessed)):
          guessed[x] = False
        blanks()
        letter = input("Guess a letter: ")
        guess(letter)
      else:
        print("Maybe some other time...")


    else:
      print("You got one!")
      letter = input("Guess again: ")
      guess(letter)
  else:
    letter = input("Sorry! Not that one. Try again: ")
    guess(letter)

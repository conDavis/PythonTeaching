answer = ["c", "o", "d", "e", "r"]
guessed = [False, False, False, False, False]

def blanks():
  result = ""
  for x in range(len(answer)):
    if guessed[x]:
      result = result + answer[x]+ " "
    else:
      result = result + "_ "
  print(result)

# recursive 
def guess(letter):
  if letter in answer:
    for x in range(len(answer)):
      if answer[x] == letter:
        guessed[x] = True
    ascii(getCorrect())
    blanks()
    if getCorrect() < 5 : 
      letter = input("You got one! Guess another letter. ")
      guess(letter)
    else : 
      print("You got it! Pull-Up Man did a pull-up!")
  else:
    letter = input("Not that letter! Guess again. ")
    guess(letter)


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


def getCorrect():
  count = 0
  for x in range(len(answer)):
    if guessed[x]:
      count = count + 1
  return count
  
        
#script
wannaPlay = input("Do you want to play a game of pull-up man with me? ")
if wannaPlay == "yes" or wannaPlay == "Yes":
  blanks()
  letter = input("Guess a letter. ")
  guess(letter)
def play():
  start = input("Do you want to play a game of pull up man?")
  if start == "yes"or start == "Yes":
    blanks() 
    letter = input("Guess a letter. ")
    guess(letter)
  else: 
    print("Okay maybe another time...")

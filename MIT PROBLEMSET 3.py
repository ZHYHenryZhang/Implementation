

def getAvailableLetters(lettersGuessed):
  import string
  notguessed = string.ascii_lowercase
  notGuessed = list(notguessed)
  # print(notguessed, "list", notGuessed, lettersGuessed)
  for x in lettersGuessed:
    notGuessed.remove(x)
  notGuessed_string = ''.join(notGuessed)
  return notGuessed_string


def isWordGuessed(secretWord, lettersGuessed):
  for x in secretWord:
    if x not in lettersGuessed:
      return False
  return True

def getGuessedWord(secretWord, lettersGuessed):
  guessedWord = []
  for x in secretWord:
    if x in lettersGuessed:
      guessedWord.append(x)
    else:
      guessedWord.append('-')
  guessedWord_string = ''.join(guessedWord)
  return guessedWord_string

def differentLetters(secretWord):
  import string
  allletters = string.ascii_lowercase
  allLetters = list(allletters)
  print("before remove", secretWord, allLetters)
  for x in list(allletters): # what if we use for x in AllLetters: here? # hard bug!!!
    print(x)
    if x not in list(secretWord):
      allLetters.remove(x)
    print(allLetters)
  print("after remove", secretWord, allLetters)
  return len(allLetters)

def setcounter(mode, secretWord):
  if mode == 1:
    return 7
  elif mode == 3:
    difnum = differentLetters(secretWord)
    if difnum > 7:
      return difnum
    else:
      return 7
# secretWord = ['a','i','s','l','i','n','g']
# lettersGuessed = ['i',]
# print(getAvailableLetters(lettersGuessed))
# print(getGuessedWord(secretWord, lettersGuessed))

# select mode
mode = int(input("Please select a mode:\n1.7 chance fixed\n2.unlimited chance\n3.dynamic\n"))
while mode not in [1,2,3]:
  mode = int(input("Please select a mode:\n1.7 chance fixed\n2.unlimited\n3.dynamic\n"))


# get the secretWord from input
secretWord = input("Please input a secret word: ")
print("flush the screen to hide your input~ \n\n\n\n\n\n\n\n\n\n ")
lettersGuessed = []
counter = setcounter(mode, secretWord)

# start the guess
while not counter == 0 and not isWordGuessed(secretWord, lettersGuessed):
  if not mode == 2:
    print(counter, "guesses left")
  print("letters guessed: ",lettersGuessed)
  print("letters not guessed: ",getAvailableLetters(lettersGuessed))
  letter = input("Please select a letter from the above list: ")
  while letter in lettersGuessed or len(letter) is not 1 :
    letter = input("Please select a letter from the above list: ")
  lettersGuessed.append(letter)
  print(getGuessedWord(secretWord,lettersGuessed))
  if not mode == 2:
    counter -=1
if isWordGuessed(secretWord, lettersGuessed):
  print("Con!, you get the right word!")
else:
  print("Game over!")
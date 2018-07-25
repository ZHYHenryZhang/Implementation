

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
  """ function: get all distinct letters in secretword
      input: a string
      return: the number of different words secretWord
  """
  import string
  allletters = string.ascii_lowercase
  allLetters = list(allletters)
  # print("before remove", secretWord, allLetters) # for debug
  for x in list(allletters): # what if we use for x in AllLetters: here? # hard bug!!!
    # print(x) # for debug
    if x not in list(secretWord):
      allLetters.remove(x)
    # print(allLetters) # for debug
  # print("after remove", secretWord, allLetters) # for debug
  return len(allLetters)

def setcounter(mode, secretWord):
  """ function: return the chance based on the mode and lenth of secret word
      input: mode and secretWord
      return: a number denote chances
  """
  if mode == 1 or mode == 0:
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
mode = 0
mode = int(input("Please select a mode:\n0.default\n1.7 chance fixed\n2.unlimited chance\n3.dynamic\n"))
while mode not in [0,1,2,3]:
  mode = int(input("Oops, please select a mode:\n0.default\n1.7 chance fixed\n2.unlimited\n3.dynamic\n"))


# get the secretWord from input
secretWord = input("Please input a secret word: ")
secretWord = secretWord.lower()
print("flush the screen to hide the input~ \n\n\n\n\n\n\n\n\n\n ")
lettersGuessed = []
counter = setcounter(mode, secretWord)

# start the guess
while not counter == 0 and not isWordGuessed(secretWord, lettersGuessed):
  if not mode == 2:
    print(counter, "guesses left")
  print("letters guessed: ",lettersGuessed)
  print("letters not guessed: ",getAvailableLetters(lettersGuessed))
  letter = input("Please select a letter from the above list: ")
  letter = letter.lower()
  while letter in lettersGuessed or len(letter) is not 1 :
    letter = input("Your letter not in above list, please select a letter from the above list: ")
  lettersGuessed.append(letter)
  print(getGuessedWord(secretWord,lettersGuessed))
  if not mode == 2: # unlimited chance for mode 2
    counter -=1
  if mode == 0 and letter in secretWord: # do not decrease for correct guess in mode 0
    counter +=1
if isWordGuessed(secretWord, lettersGuessed):
  print("Con!, you get the right word!")
else:
  print("Game over!")
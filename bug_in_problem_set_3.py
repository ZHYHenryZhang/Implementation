""" I wish to get all different letters in secretword and come up with two solutions
    both contain bugs
    debug hint is in this file being comment as last
    and the correct version is in my game file
    """



def getAvailableLetters(lettersGuessed):
  import string
  notguessed = string.ascii_lowercase
  notGuessed = list(notguessed)
  # print(notguessed, "list", notGuessed, lettersGuessed)
  for x in lettersGuessed:
    notGuessed.remove(x)
  notGuessed_string = ''.join(notGuessed)
  return notGuessed_string



def differentLetters(secretWord):
  """ function: get all distinct letters in secretword
      input: a string
      output: a list of letters
  """
  import string
  allletters = string.ascii_lowercase
  allLetters = list(allletters)
  for x in allLetters: # what if we use for x in AllLetters: here? # hard bug!!!
    if x not in list(secretWord):
      allLetters.remove(x)
  return allLetters

def notsmartmethods(secretWord):
  return getAvailableLetters(list(getAvailableLetters(list(secretWord))))


# bug one

print("Hello, bug one is here!")
secretWord = ['a','i','s','l','i','n','g']
lettersGuessed = ['i','l']
print(secretWord)
print(differentLetters(secretWord))
print("Oops, the output is so wired! Figure out why with debugging methods and correct it!")

# bug two
""" the idea is that we can get available letters from secretWord( replacing guessedletters), 
    and we do this twice to get all distinct letters in secretWord
    """

#print("Note that here is bug two! figure out why this method is stupid!")
#print(notsmartmethods(secretWord)) 

























"""
# lots of print are added for debug as you can see

def differentLetters(secretWord):
  import string
  allletters = string.ascii_lowercase
  allLetters = list(allletters)
  # print("before remove", secretWord, allLetters) # for debug
  for x in allLetters: 
    # print(x) # for debug
    if x not in list(secretWord):
      allLetters.remove(x)
    # print(allLetters) # for debug
  # print("after remove", secretWord, allLetters) # for debug
  return len(allLetters)

  """
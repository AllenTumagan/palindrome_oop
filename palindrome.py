# Ask for user input 
word = input("Input a any word: ")

# Declaring needed variables
wordList = []
reversedList = []
reversedWord = ""

# A fuction to convert string to list using for loop
def word_to_list(word):
    
    for char in word:
        wordList.append(char)
    
    return wordList

# A fuction for reversing the list using for loop
def reversed_list():
    for i in range(len(wordList)):
        char = wordList.pop()
        reversedList.append(char)
    
    return reversedList

# A function for converting the list to string usign function join()
def list_to_word():
    return reversedWord.join(reversedList)

# Calling all the functions
word_to_list(word)
reversedList = reversed_list()
reversedWord = list_to_word()

# Check if the word is a palindrome word
if reversedWord == word:
    print("Result: " + reversedWord)
    print(word + " is a palindrome word.")
else:
    print("Result: " + reversedWord)
    print(word + " is not a palindrome word.")
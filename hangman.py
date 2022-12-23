import nltk
from nltk.corpus import words

def filter_words(word, letters):
    # Get the set of unique letters in the word
    word_set = set(word)
    
    # Check if all the letters in the word are in the given list of letters
    if word_set.issubset(letters):
        return [word]
    else:
        return []

def main():
    # Get the word to be solved and the number of tries from the user
    word = input('Enter the word to be solved: ').lower()
    tries = int(input('Enter the number of tries: '))
    
    # Convert the word to a set of unique letters
    word_set = set(word)
    
    # Initialize a list to store the letters that have been guessed
    letters = []
    
    # Initialize a list to store the words that can be formed using the given letters
    word_list = words.words()
    
    # Play the hangman game until the word is solved or the user runs out of chances
    while tries > 0:
        # Filter the list of words using the function from step 2
        word_list = [w for w in word_list if filter_words(w, letters)]
        
        # Check if the list of words contains only one word
        if len(word_list) == 1:
            print(f'The word is "{word_list[0]}". You won!')
            break
        
        # Get a letter from the alphabet
        letter = chr(ord('a') + tries - 1)
        
        # Add the letter to the list of letters that have been guessed
        letters.append(letter)
        
        # Decrement the number of tries
        tries -= 1
        
    # If the word was not solved, print a message
    if tries == 0:
        print('You lost!')

main()

# Finding the Middle Character of a Word

This Python script demonstrates how to find the middle character(s) of a given word. It's designed to work with both odd and even-length word

## Explanation
The getmiddlecharacters function takes a word as input. 
It calculates the length of the word and the index of the middle character(s) using integer division (//).
If the length of the word is odd, it returns the middle character.
If the length of the word is even, it returns the middle two characters using slicing.
### Function Signature
python
def get_middle_characters(word):
    
    Returns the middle character or characters of a word.

    Parameters:
    - word (str): The input word.

    Returns:
    - str: The middle character(s) of the word.
    
 
## Example 

Suppose you want to find the middle character(s) of the word "Keyboard". 
The script will output: `Middle character(s) of the word: `bo'.

 




# Write a program that asks the user to input a string and then
# prints out the counts of each character used in the string.
#
# For example, if the input string is 'hello, world!' the output
# should be something like
#
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ',': 1
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1
# '!': 1
#
# You don't have to match this format exactly, but it's important
# for the autograder that the message you print contains
# each of the character/count pairs in the following format.
# 
# '<character>': <count>
#
# You should get input from the user using the input function. Your
# code should work for arbitrary strings, including the empty string.

def char_counter():
    print ("Please enter a word or phrase:")
    word_or_phrase = input ('')
    word_or_phrase = list(word_or_phrase)
    character_dict = {}
    for char in word_or_phrase:
        character_dict[char] = character_dict.get(char, 0) + 1
    for key, val in character_dict.items():
        print("'" + str(key) + "' : " + str(val) + '    ')
               
               
if __name__ == "__main__":
    char_counter()
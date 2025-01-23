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
    word_or_phrase = input ()
    characters = []
    count = []
    for i in range(len(word_or_phrase)):
        if word_or_phrase[i] not in characters:
            characters = characters + [word_or_phrase[i]]
    word_or_phrase = list(word_or_phrase)
    for i in range(len(characters)):
        word_or_phrase.remove(characters[i])
        variable = 1
        while characters[i] in word_or_phrase:
            word_or_phrase.remove(characters[i])
            variable = variable + 1
        count = count + [variable]
    for i in range(len(characters)):
        print ("'" + characters[i] + "' : " + str(count[i]) + '  ')
    

if __name__ == "__main__":
    char_counter()
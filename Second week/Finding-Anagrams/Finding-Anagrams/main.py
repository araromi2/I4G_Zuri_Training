# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here

    return cleanstring(word1)==cleanstring(word2)

def cleanstring(word):
    word = word.lower().split(" ")
    word = sorted("".join(word))

    return word
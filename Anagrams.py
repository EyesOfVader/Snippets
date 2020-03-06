import re
import random


def check_anagram(word1, word2):
    """
    Given two strings, returns whether they are anagrams of each other. Ignores capitalisation, spaces and punctuation
    """
    # Replaces any non-letter characters and changes the strings to lower case
    word1 = re.sub('\W', '', word1.lower())
    word2 = re.sub('\W', '', word2.lower())
    # Sorts both words and returns whether they are now equal
    return sorted(word1) == sorted(word2)


def generate_anagram(word):
    """
    Given one word string, returns an anagram of that word
    """
    # Convert the word to a list or characters
    word_list = list(word)
    # Shuffle the list
    random.shuffle(word_list)
    # Join the characters back into a string
    return ''.join(word_list)

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from english_words import english_words_set
import random


def get_word(num):
    while 1:
        word_suggestion = random.sample(english_words_set, 1)
        if len(word_suggestion[0]) == num:
            return word_suggestion
    return word_suggestion

print(get_word(15))
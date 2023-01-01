from english_words import english_words_set
import random

def is_vertical():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False


def get_position(word):
    if is_vertical():
        vertical_coordinate = [random.randint(0, 14 - len(word)), random.randint(0, 14)]
        coordinates = []
        for j in range(len(word)):
            coordinates.append([vertical_coordinate[0] + j, vertical_coordinate[1]])
        return coordinates
    else:
        horizontal_coordinate = [random.randint(0, 14), random.randint(0, 14 - len(word))]
        coordinates = []
        for j in range(len(word)):
            coordinates.append([horizontal_coordinate[0], horizontal_coordinate[1] + j])
        return coordinates



def get_puzzle():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    screen = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    ]
    list_of_word = []
    for word_to_print in random.sample(english_words_set, 500):
        if len(word_to_print) < 14 and word_to_print[0].islower() :
            start_position = get_position(word_to_print)
            reference = ''
            for i in word_to_print:
                reference += '-'
            appendix = []
            for i in range(len(word_to_print)):
                appendix.append(screen[start_position[i][0]][start_position[i][1]])
            if ''.join(appendix) == reference:
                for i in range(len(word_to_print)):
                    screen[start_position[i][0]][start_position[i][1]] = word_to_print[i]
                list_of_word.append(word_to_print)

    for row in range(len(screen)):
        for space in range(len(screen[row])):
            if screen[row][space] == '-':
                screen[row][space] = random.choice(letters)

    return screen, len(list_of_word), list_of_word

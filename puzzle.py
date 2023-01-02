from english_words import english_words_set
import random

def is_vert():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False


def get_pos(word):
    if is_vert():
        vert_coord = [random.randint(0, 14 - len(word)), random.randint(0, 14)]
        coords = []
        for j in range(len(word)):
            coords.append([vert_coord[0] + j, vert_coord[1]])
        return coords
    else:
        horiz_coord = [random.randint(0, 14), random.randint(0, 14 - len(word))]
        coords = []
        for j in range(len(word)):
            coords.append([horiz_coord[0], horiz_coord[1] + j])
        return coords



def get_puzzle():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    screen = [['-' for x in range(15)] for y in range(15)]
    list_of_word = []
    for word in random.sample(english_words_set, 500):
        if len(word) < 14 and word[0].islower():
            if len(word) >= 2 and "'" not in word:
                start_pos = get_pos(word)
                reference = ''
                for i in word:
                    reference += '-'
                appendix = []
                for i in range(len(word)):
                    appendix.append(screen[start_pos[i][0]][start_pos[i][1]])
                if ''.join(appendix) == reference:
                    for i in range(len(word)):
                        screen[start_pos[i][0]][start_pos[i][1]] = word[i]
                    list_of_word.append(word)

    for row in range(len(screen)):
        for space in range(len(screen[row])):
            if screen[row][space] == '-':
                screen[row][space] = random.choice(letters)
    return screen, list_of_word

from english_words import english_words_set
import random


def get_pos(word):
    if random.choice([True, False]):
        vert_coord = [random.randint(0, 14 - len(word)), random.randint(0, 14)]
        coords = []
        for j in range(len(word)):
            coords.append([vert_coord[0] + j, vert_coord[1]])
        return coords
    else:
        hori_coord = [random.randint(0, 14), random.randint(0, 14 - len(word))]
        coords = []
        for j in range(len(word)):
            coords.append([hori_coord[0], hori_coord[1] + j])
        return coords


def get_puzzle():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    puzzle = [['-' for x in range(15)] for y in range(15)]
    words_list = []
    for word in random.sample(english_words_set, 500):
        if len(word) < 14 and word[0].islower():
            if len(word) >= 2 and "'" not in word:
                start_pos = get_pos(word)
                reference = ''
                for i in word:
                    reference += '-'
                appendix = []
                for i in range(len(word)):
                    appendix.append(puzzle[start_pos[i][0]][start_pos[i][1]])
                if ''.join(appendix) == reference:
                    for i in range(len(word)):
                        puzzle[start_pos[i][0]][start_pos[i][1]] = word[i]
                    words_list.append(word)

    for row in range(len(puzzle)):
        for space in range(len(puzzle[row])):
            if puzzle[row][space] == '-':
                puzzle[row][space] = random.choice(letters)
    return puzzle, words_list

# Given a boolean function is_word(w) function, implement get_words(keysPressed)
# which returns the words that can be spelled using the phone number pad mapping.
from typing import List
# example input: [2,2,8]
# example output: ['CAT', 'BAT', 'ACT']

def get_words(keysPressed: List[int]) -> List[str]:
    let_table = {2: 'ABC',
                 3: 'DEF',
                 4: 'GHI',
                 5: 'JKL',
                 6: 'MNO',
                 7: 'PQRS',
                 8: 'TUV',
                 9: 'WXYZ'}
    # checking all possible combinations for each num in keysPressed
    mapped_vals = [let_table[num] for num in keysPressed]
    # print(mapped_vals)
    output = []
    long_string = ''
    # join everything into one long string
    print(mapped_vals)
    max_count = len(keysPressed)
    # have two pointers'
    word = ''
    ii = 0
    while ii < max_count:
        word = ''
        for jj in range(max_count):
            word += mapped_vals[jj][ii]
      # if is_word(word):
        output.append(word)
        ii += 1

    print(output)
    '''
    for ii, combo in enumerate(mapped_vals):
      output_string = combo[ii]
      for xx in len(combo):
    '''


def letterCombinations(digits):
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    finalRes = []
    currRes = []

    for i, num in enumerate(digits):
        if i == 0:
            for char in letters[num]:
                currRes.append(char)
        else:
            for k in range(len(finalRes)):
                for c in letters[num]:
                    combo = finalRes[k] + c
                    currRes.append(combo)

        finalRes = currRes
        currRes = []

    return finalRes




test_input = [2, 2, 8]
get_words(test_input)

'''
def is_word(w: List[str]):
  return w == valid_word

'''

#!/usr/bin/python3

'''
I use brackets to tell the user if the guess is correct
[] for the green color
<> for yellow
() for grey
^behavior for these is the same as scoredle
'''

import random

GUESS_FILE = "wordle-nyt-allowed-guesses.txt"
ANSWER_FILE = "wordle-nyt-answers-alphabetical.txt"

def open_file(name):
    try:
        res = open(name, "r")
        return res.readlines()
    except FileNotFoundError:
        print(f"File {name} not found.")

def get_guess(prompt):
    res = input(prompt + "\n")
    if len(res) != 5:
        return get_guess("Incorrect length")
    return res.lower()

def get_hist(word):
    res = {}
    for letter in word:
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1
    return res

def grade_guess(guess, answer):
    out = ""
    cpy = ""
    
    ahist = get_hist(answer)
    correct_cnt = 0
    for i in range(len(guess)):
        cur = guess[i]
        if cur == answer[i]:
            out += '[' + cur + ']'
            cpy += cur
            correct_cnt += 1
            if correct_cnt == 5:
                print(out)
                return True
            continue
        if cur in answer:
            if get_hist(cpy).get(cur, 0) < ahist.get(cur, 0):
                out += '<' + cur + '>'
                cpy += cur
                continue
        out += '(' + cur + ')'
    print(out)
    return False

def play(allowed, answer):
    #print(f"Answer is {answer}")
    n = 0
    print(" _  _  _  _  _")
    while True:
        guess = get_guess("")
        if guess not in allowed:
            print("Not in word list")
            continue
        if grade_guess(guess, answer):
            break
        n += 1
        if n == 6:
            print("\nFailed:")
            grade_guess(answer, answer)
            break

def main():
    answers = [x.rstrip() for x in open_file(ANSWER_FILE)]
    answer = random.choice(answers)
    guesses = [x.rstrip() for x in open_file(GUESS_FILE)]
    all_allowed = answers + guesses
    play(all_allowed, answer)

if __name__ == "__main__":
    main()


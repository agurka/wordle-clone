#!/usr/bin/python3

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
        return get_guess(prompt)
    return res

def play(allowed, answer):
    print(f"Answer is {answer}")
    n = 0
    while True:
        current = "_ _ _ _ _"
        guess = get_guess(current)
        if guess == answer:
            print("CORRECT!")
            return
        if guess not in allowed:
            print("Not in word list")
            continue


def main():
    answers = [x.rstrip() for x in open_file(ANSWER_FILE)]
    answer = random.choice(answers)
    guesses = [x.rstrip() for x in open_file(GUESS_FILE)]
    all_allowed = answers + guesses
    print(type(all_allowed))

    play(all_allowed, answer)


if __name__ == "__main__":
    main()


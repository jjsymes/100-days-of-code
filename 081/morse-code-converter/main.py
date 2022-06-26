#!/usr/bin/env python3

import sys
import argparse

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' / '
}

def get_user_input():
    user_input = input("Enter a string to convert to morse code: ")
    return user_input


def text_to_morse(text: str) -> str:
    morse_code = ""
    for char in text:
        morse_code += MORSE_CODE[char.upper()] + " "
    return morse_code.strip()


def main():
    parser = argparse.ArgumentParser(description='Convert text to morse code')
    parser.add_argument("-t", "--text", metavar='text', type=str, help='text to convert')
    args = parser.parse_args()
    if args.text:
        text = args.text
    else:
        text = get_user_input()

    try:
        morse = text_to_morse(text)
    except KeyError:
        print("Invalid input")
        sys.exit(1)
    else:
        print(morse)
        sys.exit(0)


if __name__ == "__main__":
    main()


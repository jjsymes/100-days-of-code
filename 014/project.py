from art import logo, vs
from game_data import data
import random
import os


def generate_celeb_pair(celeb_1=None):
    celebs = []
    if celeb_1 == None:
        celeb_1 = random.choice(data)
    celeb_2 = random.choice(data)
    celebs = [celeb_1, celeb_2]
    if celeb_1 == celeb_2 or celeb_1.get("follower_count") == celeb_2.get("follower_count"):
        celebs = generate_celeb_pair(celeb_1)
    return celebs


def construct_celeb_string(celeb):
    name = celeb.get("name")
    description = celeb.get("description")
    country = celeb.get("country")
    string = name + ", a " + description + ", from " + country + "."
    return string


def clear_screen():
    os.system('clear' if os.name =='posix' else 'cls')


def get_correct_choice(celeb_1, celeb_2):
    if celeb_1.get("follower_count") > celeb_2.get("follower_count"):
        return "a"
    else:
        return "b"


def game(score=0, last_celeb=None):
    clear_screen()
    score = score
    celeb_pair = generate_celeb_pair(last_celeb)
    celeb_1 = celeb_pair[0]
    celeb_2 = celeb_pair[1]

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {construct_celeb_string(celeb_1)}")
    print(vs)
    print(f"Against B: {construct_celeb_string(celeb_2)}")

    valid_input = False
    while not valid_input:
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player_choice in ["a", "b"]:
            valid_input = True
        else:
            pass

    correct_choice = get_correct_choice(celeb_1, celeb_2)

    if player_choice == correct_choice:
        score += 1
        game(score, celeb_2)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


game()
import random
from people_data import people
import art


# const


TESTING = True


# functions


def clr():
    print('\n' * 20)


def get_random_person():
    return random.choice(people)


def fill_second_person(arr):
    p2 = get_random_person()
    while p2 == arr[0]:
        p2 = get_random_person()

    if len(arr) > 1:
        arr[1] = p2
    else:
        arr.append(p2)    


def show_question(persons):
    print(f"Compare A: {persons[0]["name"]}, "
          f"{persons[0]["profession"]}, "
          f"from {persons[0]["country"]}.")

    print(art.logo_vs)

    print(f"Against B: {persons[1]['name']}, "
          f"{persons[1]['profession']}, "
          f"from {persons[1]['country']}.")

    if TESTING:
        test_winner = max(persons, key=lambda n: n['followers'])
        print(f"(winner = '{test_winner["name"]}')")


def get_answer():
    answer = ""
    print("")
    while answer.lower() != 'a' and answer.lower() != 'b':
        answer = input("Who has more followers? Type 'A' or 'B': ")
    return answer.lower()


def play_game():
    score = 0
    game_over = False

    two_persons = [get_random_person()]
    fill_second_person(two_persons)

    while game_over is False:
        clr()
        print(art.logo)

        if score > 0:
            print(f"You're right! Current score: {score}.")

        show_question(two_persons)
        answer = get_answer()

        if (
            answer == 'a' and two_persons[0]['followers'] > two_persons[1]['followers']) or (
            answer == 'b' and two_persons[1]['followers'] > two_persons[0]['followers']
        ):
            score += 1
            two_persons[0] = two_persons[1]
            fill_second_person(two_persons)

        else:
            game_over = True
            print(f"\nGAME OVER! You ended with score {score}. Congratulations.")


# code


play_game()

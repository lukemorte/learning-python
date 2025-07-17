import random
from people_data import people
import art


# functions


def test():
    for man in people:
        print(
            f"{man['name']}, {man['profession']}, from {man['country']} ... "
            f"{man['followers']}"
        )


def clr():
    print('\n' * 20)


def get_random_person():
    return random.choice(people)


def show_question(persons):
    clr()
    print(art.logo)

    print(f"Compare A: {persons[0]["name"]}, "
          f"{persons[0]["profession"]}, "
          f"from {persons[0]["country"]}.")

    print(art.logo_vs)

    print(f"Against B: {persons[1]['name']}, "
          f"{persons[1]['profession']}, "
          f"from {persons[1]['country']}.")


def get_answer():
    answer = ""
    print("")
    while answer.lower() != 'a' and answer.lower() != 'b':
        answer = input("Who has more followers? Type 'A' or 'B': ")
    return answer.lower()

# vars


score = 0


# code


two_persons = [get_random_person(), get_random_person()]
show_question(two_persons)

answer = get_answer()

if (answer == 'a' and two_persons[0]['followers'] > two_persons[1]['followers']) or (answer == 'b' and two_persons[1]['followers'] > two_persons[0]['followers']):
    score += 1
    two_persons[0] = two_persons[1]
    two_persons[1] = get_random_person()
    show_question(two_persons)

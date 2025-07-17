import random
from people_data import people
import art


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
    print(f"Compare A: {persons[0]["name"]}, "
          f"{persons[0]["profession"]}, "
          f"from {persons[0]["country"]}.")

    print(art.logo_vs)

    print(f"Compare B: {persons[1]['name']}, "
          f"{persons[1]['profession']}, "
          f"from {persons[1]['country']}.")


clr()
# print(art.logo)
# print("")
# print(art.logo_vs)


two_persons = [get_random_person(), get_random_person()]


show_question(two_persons)

from people_data import people


for man in people:
    print(
        f"{man['name']}, {man['profession']}, from {man['country']} ... "
        f"{man['followers']}"
    )

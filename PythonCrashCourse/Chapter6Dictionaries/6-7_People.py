first_person = {'first_name': 'Angus', 'last_name': 'Cheng', 'age': 20, 'city': 'Brisbane' }
second_person  = {'first_name': 'Jerry', 'last_name': 'Hao', 'age': 43, 'city': 'Japan' }
third_person  = {'first_name': 'Reagan', 'last_name': 'Chu', 'age': 16, 'city': 'Hong Kong' }
people = [first_person, second_person, third_person]
for person in people:
    print(f"This person\'s name is {person['first_name']} {person['last_name']}, is {person['age']} and is from {person['city']}")
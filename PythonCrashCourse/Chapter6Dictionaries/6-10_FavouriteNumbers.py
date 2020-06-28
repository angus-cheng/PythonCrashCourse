favourite_numbers = {'Dex': [3, 44], 
    'Angus': [7,28, 49, 100], 
    'Jock': [1, 20, 80, 90], 
    'Lain': [30, 0, 804, 1234], 
    'Fred': [99, 78, 39, 4, 12, 49, 28]}

for person, numbers in favourite_numbers.items():
    print(f'\n{person} has {len(numbers)} favourite numbers. They are ')

    for i in numbers:
        print(f'\t{i}')
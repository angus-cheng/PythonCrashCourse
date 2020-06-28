favourite_places = {'Jason': ['Australia', 'Japan', 'South Africa'],
    'Angus': ['Canada', 'Japan', 'Italy'],
    'Dex': ['America', 'Greenland', 'England']
    }

for person, places in favourite_places.items():
    print(f"\n{person}'s favourite places in the world are")

    for place in places:
        print(f'\t{place}')
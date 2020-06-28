cities = {
    'Melbourne': {
        'Country': 'Australia',
        'Population': 4_900_900,
        'Fact': 'Pretty artsy'
        },

    'Venice': {
        'Country': 'Italy',
        'Population': 262_000,
        'Fact': 'Built on more than 100 islands'
        },

    'Toronto': {
        'Country': 'Canada',
        'Population':  2_930_000,
        'Fact': 'Green space a plenty'
        }
    }

for city, info in cities.items():
    print(f"\n{city}")
    print(f"\tPopulation is {info['Population']} and interestingly, it is {info['Fact'].lower()}.")
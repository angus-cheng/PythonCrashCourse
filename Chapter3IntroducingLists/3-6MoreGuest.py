guests = ['Steve Jobs', 'Adolph Hitler', 'Mum']
print(f"Come for a dinner {guests[0]}")
print(f"Come for a dinner {guests[1]}")
print(f"Come for a dinner {guests[2]}")
print(f"Unfortunately {guests[1]} can't make it")
guests.insert(2, "Bill Gates")
print(f"Instead {guests[1]} will be coming")
print(f"Come for a dinner {guests[0]}")
print(f"Come for a dinner {guests[1]}")
print(f"Come for a dinner {guests[2]}")
print("There appears to be more guests coming as well so I've made arrangements for a bigger table")
guests.insert(0, "Matthew McConaughey")
guests.insert(2, "Angelina Jolie")
guests.append("Gal Gadot")
print(guests)
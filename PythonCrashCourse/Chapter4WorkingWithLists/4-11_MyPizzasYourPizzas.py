pizzas = ['Hawaiian', 'Pepperoni', 'Supreme']
friend_pizzas = pizzas[:]
pizzas.append('Cheese')
friend_pizzas.append('Vegetarian')
print('My favourite pizzas are ')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are")
for pizza in friend_pizzas:
    print(pizza)
pizzas = ['Hawaiian', 'Pepperoni', 'Supreme', 'Cheese', 'Vegetarian']
for pizza in pizzas:
    print(f'I like {pizza}')
print('Pizza is great')
print('The first 3 pizzas I liked are')
for pizza in pizzas[:3]:
    print(pizza)
print('Three pizzas are in the middle of the list are ')
number_of_pizza = len(pizzas)
print(number_of_pizza)
for pizza in pizzas[1 : 4]:
    print(pizza)
print('The last three pizzas in the list are')
for pizza in pizzas[-3:]:
    print(pizza)
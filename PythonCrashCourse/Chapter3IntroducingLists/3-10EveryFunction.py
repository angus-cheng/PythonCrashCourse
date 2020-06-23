motorcycles = ['Kawasaki', 'Ducati', 'Yamaha', 'Honda', 'BMW', 'Aprilia', 'Suzuki']
motorcycles.append('KTM')
motorcycles.insert(5, 'MV Augusta')
del motorcycles[0]
motorcycles.pop(0)
motorcycles.remove('BMW')
motorcycles.sort()
motorcycles.sort(reverse=True)
sorted(motorcycles, reverse=True)
motorcycles.reverse()
len(motorcycles)
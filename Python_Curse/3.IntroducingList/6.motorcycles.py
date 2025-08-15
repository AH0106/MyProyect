

motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles)


motorcycles[0] = 'modificated'
print(motorcycles)

#append()-> add elements to the end of the list

motorcycles.append('ducati')

print(motorcycles)


motorcycles.insert(0, 'toyota')

print(motorcycles)

del motorcycles[1]
print(motorcycles)


motorcycles.append('newBicycle')

print("Using pop()")

#pop()->remove the last item, but lets you work with that item after removing

popped_motorcycle = motorcycles.pop()
print(motorcycles)



print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


list_example = ['item1', 'item2', 'item3']
print(list_example)

popped_item = list_example.pop(0)
print(f"The first element of the list was {popped_item.title()}")



print('\n Removing a item by Value')

motorcycles = ['honda', 'yamaha', 'susuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)



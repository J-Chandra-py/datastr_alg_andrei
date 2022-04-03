obj1 = {'a': True, 'b': 1}
obj2 = obj1

del obj1

print(id(obj2))
print(id(obj1))
# print(id(obj1), id(obj2))
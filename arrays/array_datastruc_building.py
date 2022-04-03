class Myarray:

    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        # returns the element at index positon
        # need a print statement at the method call
        return self.data[index]

    def push(self, item):

        # No good ways for me to add an element
        # To an empty list without using append, extend
        # I think my space complexity is effected

        # Add an item to a list with a subpart-slicing assignment
        print(id(self.data))
        self.data += [item]

        # self.data[self.length : self.length] = [item]
        print(id(self.data))
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        # idea of single responsibility
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        del_item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):

        # Here the items at the right of index
        # will be shifted to left by one place.
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

        # Last value is still not disturbed
        # So we delete the last item
        del self.data[self.length - 1]
        # Decrease the length by 1 as an element is deleted
        self.length -= 1




newarray = Myarray()

newarray.push('hi')
newarray.push('there')
newarray.push('yeah')
newarray.push('you')
newarray.push('!')
newarray.push('man')
# newarray.pop()
# print(newarray.get(1))
# print(newarray.data)
# type(newarray)
newarray.delete(1)
newarray.delete(3)
print(vars(newarray))
# print(newarray.__dict__)
# import pprint
#
# pprint.pprint(vars(Myarray))
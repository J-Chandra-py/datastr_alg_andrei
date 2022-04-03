class HashTable:
    def __init__(self):
        self.data = []

    def set(self, key, value):
        self.data += [(key, value)]

    def get(self, key):
        z = tuple(filter(lambda x: x[0] == key, self.data))
        print(z)
        return z[0][1]

        # value = filter(map(lambda x: , self.data))


my_hash = HashTable()
my_hash.set('grapes', 1000)
my_hash.set('mangoes', 200)
my_hash.set('banana', 500)
my_hash.set('kiwi', 80)
print(my_hash.data)
print(f"grapes: {my_hash.get('grapes')}")
print(f"manoges: {my_hash.get('mangoes')}")
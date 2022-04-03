class Node:
    def __init__(self, value):
        self.value = value
        self.next = 0

    # return {'value': self.value, 'next': self.next}


new_node = Node(5)
a = {new_node}
new_node['next'] = {}
print(a)
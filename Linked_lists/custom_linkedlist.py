class Node:
    def __init__(self, value):
        self.node = {
            'value': value,
            'next': None
        }


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):            # ----O(1)
        # Instantiate a new node using Node class with passing the value as argument
        new_node = Node(value)
        # Now attach the new node to the tail's (next) key
        # For the beginning case, tail's (next)-key and Head's (next)-key are same
        # As, self.tail is the reference of self.head and they both point to same address
        # All modifications will be done on self.head's (next)-key
        self.tail['next'] = new_node.node
        # Make the new node updated as the tail,
        self.tail = new_node.node
        # Update the length of linked list
        self.length += 1
        return self.tail

    def prepend(self, value):             # ----O(1)
        # new_node = {'value': value, 'next': None}
        new_node = Node(value)
        # Attach the entire linked list to the (next) key of the created new_node
        new_node.node['next'] = self.head
        self.head = new_node.node
        self.length += 1
        return self.head

    def lookup(self, value):               # -----O(n)
        temp = self.head
        index = 0
        while temp['value'] != value:
            # print(temp)
            index += 1
            if index <= self.length-1:
                temp = temp['next']
            # elif index == self.length-1:
            #     temp = self.tail
            elif index > self.length-1:
                return 'Search value not in the list'

        return f"value: {value} is at index: {index}"

    def print_list(self):
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(current_node['value'])
            current_node = current_node['next']
        return values

    # index start from head with index = 0
    def insert(self, index, value):             # ----- O(n)
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        # take leader as the node before the index position
        leader = self.traverse_to_index(index-1)
        # take holding_pointer as the node after the index position
        holding_pointer = leader['next']
        leader['next'] = new_node.node
        new_node.node['next'] = holding_pointer
        # Update th length
        self.length += 1

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node['next']
            counter += 1
        return current_node

    # Removes the node at index position
    def remove(self, index):

        if index >= self.length:
            return 'index out of range'

        node_to_remove = self.traverse_to_index(index)
        leader = self.traverse_to_index(index-1)
        # Due to Garbage collection in Python as there are no pointers to node_to_remove its life ends.
        leader['next'] = node_to_remove['next']
        # Update the length of linked list
        self.length -= 1
        return f'removed node at index: {index}'


myLinkedList = LinkedList(10)
(myLinkedList.append(5))
(myLinkedList.append(16))
(myLinkedList.prepend(1))
print(myLinkedList.lookup(22))
myLinkedList.insert(0, 99)
myLinkedList.insert(54, 20)
print(myLinkedList.print_list())
print(myLinkedList.remove(2))
print(myLinkedList.print_list())
print(vars(myLinkedList))

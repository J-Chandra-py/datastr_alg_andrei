class Node:
    def __init__(self, value):
        self.node = {
            'value': value,
            'prev': None,
            'next': None
        }


class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'prev': None,
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
        # attach a pointer for prev in new_node to previous node i.e., the tail
        new_node.node['prev'] = self.tail
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
        self.head['prev'] = new_node.node
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
        if index < 0:
            return "Invalid index"
        new_node = Node(value)
        # take leader as the node before the index position
        leader = self.traverse_to_index(index-1)
        # take holding_pointer as the node after the index position
        follower = leader['next']
        leader['next'] = new_node.node
        new_node.node['prev'] = leader
        new_node.node['next'] = follower
        follower['prev'] = new_node
        # Update th length
        self.length += 1
        print(vars(self))

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node['next']
            counter += 1
        return current_node

    # Removes the node at index position
    def remove(self, index):
        # Case-1 : index out of range
        if index >= self.length:
            return 'index out of range'

        # get the node for removal using traversal function
        node_to_remove = self.traverse_to_index(index)

        # Case-2 : when we have to remove 1st element, we need a separate code
        # So as to avoid TypeError: 'NoneType' object is not subscriptable
        if index == 0:
            follower = self.traverse_to_index(index + 1)
            self.head = node_to_remove['next']
            follower['prev'] = self.head
            # need a separate return
            # So, as to avoid initiating the below lines,
            # which will result in error for case-2
            return f'removed node at index: {index}'

        leader = self.traverse_to_index(index-1)
        if index != self.length - 1:
            follower = self.traverse_to_index(index+1)
            follower['prev'] = node_to_remove['prev']

        # case -3 : to avoid error in case of removing the last element
        if index == self.length - 1:
            node_to_remove['prev'] = None
        # Due to Garbage collection in Python as there are no pointers to node_to_remove its life ends.
        leader['next'] = node_to_remove['next']

        # Update the length of linked list
        self.length -= 1
        return f'removed node at index: {index}'


# class DoublyLinkedlist(LinkedList):
#     def __init__(self, value):
#         LinkedList.__init__(self, value)
#         self.tail = {
#             'value': value,
#             'previous': None,
#             'next': None
#         }
#         self.head = self.tail
#         self.length = 1


myLinkedList = DoublyLinkedList(10)
(myLinkedList.append(5))
(myLinkedList.append(16))
myLinkedList.prepend(1)
# print(myLinkedList.lookup(22))
myLinkedList.insert(1, 99)
myLinkedList.insert(54, 20)
print(myLinkedList.print_list())
print(myLinkedList.remove(0))
print(myLinkedList.print_list())
print(myLinkedList.remove(0))
print(myLinkedList.print_list())
print(vars(myLinkedList))

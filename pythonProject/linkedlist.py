from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def prepend_node(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def contains(self, data):
        search_node = Node(data)
        temporary_node = self.head

        while temporary_node is not None:
            if temporary_node.data == search_node.data:
                return True
            temporary_node = temporary_node.next
        else:
            return False

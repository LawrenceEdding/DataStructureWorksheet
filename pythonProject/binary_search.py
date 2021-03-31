
class BinaryNode:
    def __init__(self, data):
        self.lesser_next = None
        self.greater_next = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = BinaryNode(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head
        while True:
            if node.data <= temporary_node.data:
                if temporary_node.lesser_next is not None:
                    temporary_node = temporary_node.lesser_next
                    continue
                else:
                    temporary_node.lesser_next = node
                    return
            if node.data > temporary_node.data:
                if temporary_node.greater_next is not None:
                    temporary_node = temporary_node.greater_next
                    continue
                else:
                    temporary_node.greater_next = node
                    return

    def search(self, data):
        search_node = BinaryNode(data)
        temporary_node = self.head

        while True:
            if search_node.data < temporary_node.data:
                if temporary_node.lesser_next is not None:
                    temporary_node = temporary_node.lesser_next
                    continue
                else:
                    return False
            if search_node.data > temporary_node.data:
                if temporary_node.greater_next is not None:
                    temporary_node = temporary_node.greater_next
                    continue
                else:
                    return False
            if search_node.data == temporary_node.data:
                return True  # Return the node probably.

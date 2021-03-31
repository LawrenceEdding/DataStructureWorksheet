from linkedlist import LinkedList
from binary_search import BinaryTree
import store_data_structure


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.prepend_node(42)
    if linked_list.contains(69):
        print(f'true')
    else:
        print(f'false')
    binary = BinaryTree()

    binary.insert(55)
    binary.insert(60)
    binary.insert(65)
    binary.insert(42)
    if binary.search(65):
        print(f'True')
    else:
        print(f'False')
store_data_structure.sweepstakes()
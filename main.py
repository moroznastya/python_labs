from tree import  BinarySearchTree, Resistor

if __name__ == '__main__':
    a = 5

Tree: BinarySearchTree = BinarySearchTree()
Tree.insert(Resistor("MLT", 20, 10, 4))
Tree.insert(Resistor("C2_14", 10, 10, 4))
Tree.insert(Resistor("OMLT", 25, 10, 4.6))
Tree.insert(Resistor("C2_14", 22, 10, 4))
Tree.insert(Resistor("C2_29B", 10, 10, 4))
Tree.insert(Resistor("C2_33H", 5, 10, 4))
Tree.find_and_print_node(10)
print()
Tree.print_binary_search_tree()
Tree.delete_nodes_with_type(4)
print()
Tree.print_binary_search_tree()
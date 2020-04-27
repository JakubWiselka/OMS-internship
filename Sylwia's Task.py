class BinaryTree:
    def __init__(self, value, ammount):
        self.value = value
        self.ammount = ammount
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, value, ammount):
        if self.left_child == None:
            self.left_child = BinaryTree(value, ammount)
        else:
            new_node = BinaryTree(value, ammount)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right(self, value, ammount):
        if self.right_child == None:
            self.right_child = BinaryTree(value, ammount)
        else:
            new_node = BinaryTree(value, ammount)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value, self.ammount)
        
        if self.right_child:
            self.right_child.in_order()
        
        

MPK1 = BinaryTree('MPK1', [150, 50])
MPK1.insert_left('MPK2.1', [100, 20])
MPK1.insert_right('MPK2.2', [2200])

MPK2_1 = MPK1.left_child
MPK2_1.insert_left('MPK3.1', [150])
MPK2_1.insert_right('MPK3.2', [900, 10])

MPK2_2 = MPK1.right_child
MPK2_2.insert_left('MPK3.3', [190])


MPK3_3 = MPK2_2.left_child
MPK3_2 = MPK2_1.right_child
MPK3_1 = MPK2_1.left_child



MPK2_2.in_order()








#             |MPK 1|
#             /        \
#     |MPK 2.1|         |MPK 2.2|
#    /        \           /
# |MPK 3.1|  |MPK 3.2|   |MPK 3.3|




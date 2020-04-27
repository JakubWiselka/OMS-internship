# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
        
#     def insert_left(self, value):
#         if self.left_child == None:
#             self.left_child = BinaryTree(value)
#         else:
#             new_node = BinaryTree(value)
#             new_node.left_child = self.left_child
#             self.left_child = new_node
            
#     def insert_right(self, value):
#         if self.right_child == None:
#             self.right_child = BinaryTree(value)
#         else:
#             new_node = BinaryTree(value)
#             new_node.right_child = self.right_child
#             self.right_child = new_node
            
#     def pre_order(self):
#         print(self.value)

#         if self.left_child:
#             self.left_child.pre_order()

#         if self.right_child:
#             self.right_child.pre_order()
    
#     def in_order(self):
#         if self.left_child:
#             self.left_child.in_order()

#         print(self.value)

#         if self.right_child:
#             self.right_child.in_order()
            
#####################################################
# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
        
#     def insert_node(self, value):
#         if value <= self.value and self.left_child:
#             self.left_child.insert_node(value)
#         elif value <= self.value:
#             self.left_child = BinarySearchTree(value)
#         elif value > self.value and self.right_child:
#             self.right_child.insert_node(value)
#         else:
#             self.right_child = BinarySearchTree(value)

#     def find_node(self, value):
#         if value < self.value and self.left_child:
#             return self.left_child.find_node(value)
#         if value > self.value and self.right_child:
#             return self.right_child.find_node(value)

#         return value == self.value

# bst = BinarySearchTree(15)
# bst.insert_node(10)
# bst.insert_node(8)
# bst.insert_node(12)
# bst.insert_node(20)
# bst.insert_node(17)
# bst.insert_node(25)
# bst.insert_node(19)
# print(bst.find_node(15)) # True
# print(bst.find_node(10)) # True
# print(bst.find_node(8)) # True
# print(bst.find_node(12)) # True
# print(bst.find_node(20)) # True
# print(bst.find_node(17)) # True
# print(bst.find_node(25)) # True
# print(bst.find_node(19)) # True






#############################

# a_node = BinaryTree('a')
# a_node.insert_left('b')
# a_node.insert_right('c')

# b_node = a_node.left_child
# b_node.insert_right('d')

# c_node = a_node.right_child
# c_node.insert_left('e')
# c_node.insert_right('f')

# d_node = b_node.right_child
# e_node = c_node.left_child
# f_node = c_node.right_child


# print(a_node.value) # a
# print(b_node.value) # b
# print(c_node.value) # c
# print(d_node.value) # d
# print(e_node.value) # e
# print(f_node.value) # f
# a_node.pre_order




##############################







##################################################### EXAMPLE 2 #################################################

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inOrder_print(tree.root, "")
        else:
            print("error")
            
        
        
                #         1
                #       /   \
                #     2       3
                #    / \     / \
                #   4   5   6   7
                
                #   1-2-4-5-3-6-7   preorder
                #   4-2-5-1-6-3-7   inorder
                
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    
    
    
    
    
    def inOrder_print(self, start, traversal):
        if start:
            traversal = self.inOrder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal =self.inOrder_print(start.right, traversal)
        return traversal

    

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.printTree("inorder"))
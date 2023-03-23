# I will implement a simple binary search tree in python
# we start off with a root node (lets say 6), in a binary search tree
# as we go deeper into the tree , every value less than the root/parent node will be on the left side
# every value greater than or equal to the root/parent node will be on the right side
# each child node can be viewed as its own binary tree, to make the function recursive, same rules apply

class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        
        # in order traversal, calls each node's value in numerical order
    def in_orderTraversal(self):
        # first we will go as far left as possible
        # if we cant go left anymore, we call print()
        # then we traverse as far right as possible 
        if self.left: # if left node exists
            self.left.in_orderTraversal()
        print(self.value)
        if self.right:
            self.right.in_orderTraversal()

    #pre order traversal
    def pre_orderTraversal(self):
        # we print the value first
        print(self.value)
        if self.left: # if left node exists
            self.left.pre_orderTraversal()
        if self.right:
            self.right.pre_orderTraversal()
    
    #post order traveral
    def post_orderTraversal(self):
        if self.left:
            self.left.post_orderTraversal()
        if self.right:
            self.right.post_orderTraversal()
        print(self.value)


# root node
tree = TreeNode(6)
# iserting values after our root node
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

tree.in_orderTraversal()
print("end")
tree.pre_orderTraversal()
print("end")
tree.post_orderTraversal()
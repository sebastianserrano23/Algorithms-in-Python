#i will implement a simple binary search tree in python
# we start off with a root node (lets say 6), in a binary search tree
# as we go deeper into the tree , every value less than the root/parent node will be on the left side
# every value greater than or equal to the root/parent node will be on the right side
# each child node can be viewed as its own binary tree, to make the function recursive, same rules apply


from asyncio.windows_events import NULL


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
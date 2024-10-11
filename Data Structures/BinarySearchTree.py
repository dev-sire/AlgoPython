class Tree:
    def __init__(self, val=None) -> None:
        self.value = val

        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    
    def isEmpty(self):
        return (self.value == None)

    def isleaf(self):
        # Check if the tree node is a leaf node (both left and right children are None)
        if self.left.left == None and self.right.right == None:
            return True
        else:
            return False
    
    def insert(self, data):
        if self.isempty():
            # If the current node is empty, insert the data as its value
            self.value = data
            # Create empty left and right children
            self.left = Tree()
            self.right = Tree()
        elif self.value == data:
            # If the data already exists in the tree, return
            return
        elif data < self.value:
            # If the data is less than the current node's value, insert it into the left subtree
            self.left.insert(data)
            return
        elif data > self.value:
            # If the data is greater than the current node's value, insert it into the right subtree
            self.right.insert(data)
            return
        
    def find(self, v):
        if self.isEmpty():
            print("{} is not found".format(v))
            return False
        if self.value == v:
            print("{} is found".format(v))
            return True
        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)
        
    def inorder(self):
        if self.isempty():
            # If the tree is empty, return an empty list
            return []
        else:
            # Return the inorder traversal of the tree (left subtree, root, right subtree)
            return self.left.inorder() + [self.value] + self.right.inorder()
        
    def maxval(self):
        # Find the maximum value in the Tree
        if self.right.right == None:
            return (self.value)
        else:
            return (self.right.maxval())
    
    def delete(self, v):
    # Delete a value from the Tree
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return
            
# Test the Tree class
t = Tree(15)
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)
print("Before deleting 4: ")
print(t.inorder())
t.delete(4)
print("After deleting 4: ")
print(t.inorder())
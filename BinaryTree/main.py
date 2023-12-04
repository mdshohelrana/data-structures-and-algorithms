class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)
    
    def insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=' ')

tree = BinaryTree()
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(8)

print("In-order Traversal:")
tree.inorder_traversal(tree.root)

print("\nPre-order Traversal:")
tree.preorder_traversal(tree.root)

print("\nPost-order Traversal:")
tree.postorder_traversal(tree.root)
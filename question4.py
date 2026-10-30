class Node:
    """Represents a node in a Binary Search Tree."""

    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.left = None
        self.right = None


class BST:
    """Represents a Binary Search Tree."""

    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, data):
        """Insert a value into the BST using recursion."""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, root, data):
        """Recursively insert a value into the correct position."""
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert_recursive(root.left, data)
        elif data > root.data:
            root.right = self._insert_recursive(root.right, data)

        return root

    def inorder(self):
        """Perform an in-order traversal of the BST."""
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        """Recursively visit nodes in left-root-right order."""
        if root is not None:
            self._inorder_recursive(root.left)
            print(root.data, end=" ")
            self._inorder_recursive(root.right)


# Example usage
bst = BST()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order traversal:")
bst.inorder()
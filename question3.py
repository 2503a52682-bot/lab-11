class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class LinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the linked list.

        Args:
            data: The value to be inserted into the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        """Display all elements of the linked list."""
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example usage
linked_list = LinkedList()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

print("Linked List:")
linked_list.display()
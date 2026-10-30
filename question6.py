from collections import deque


class DequeDS:
    """A double-ended queue implementation using collections.deque."""

    def __init__(self):
        """Initialize an empty deque."""
        self.deque = deque()

    def insert_front(self, item):
        """Insert an item at the front of the deque.

        Args:
            item: The item to be inserted.
        """
        self.deque.appendleft(item)

    def insert_rear(self, item):
        """Insert an item at the rear of the deque.

        Args:
            item: The item to be inserted.
        """
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the item from the front.

        Returns:
            The item removed from the front.

        Raises:
            IndexError: If the deque is empty.
        """
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque.popleft()

    def remove_rear(self):
        """Remove and return the item from the rear.

        Returns:
            The item removed from the rear.

        Raises:
            IndexError: If the deque is empty.
        """
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque.pop()

    def display(self):
        """Display all elements in the deque."""
        print("Deque:", list(self.deque))


# Example usage
d = DequeDS()

d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)
d.insert_rear(30)

d.display()

print("Removed from front:", d.remove_front())
print("Removed from rear:", d.remove_rear())

d.display()
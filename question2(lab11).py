class Queue:
    """A simple FIFO-based queue using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.items:
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if not self.items:
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# Example usage
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:", queue.items)
print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Queue size:", queue.size())
print("Queue:", queue.items)
import heapq


class PriorityQueue:
    """A priority queue implemented using the heapq module."""

    def __init__(self):
        """Initialize an empty priority queue."""
        self.queue = []

    def enqueue(self, item, priority):
        """Add an item to the queue with a given priority.

        Args:
            item: The item to be added.
            priority (int): Priority of the item. Higher number means
                            higher priority.
        """
        heapq.heappush(self.queue, (-priority, item))

    def dequeue(self):
        """Remove and return the item with the highest priority.

        Returns:
            The item with the highest priority.

        Raises:
            IndexError: If the priority queue is empty.
        """
        if not self.queue:
            raise IndexError("Priority queue is empty")

        priority, item = heapq.heappop(self.queue)
        return item

    def display(self):
        """Display all items in the priority queue."""
        if not self.queue:
            print("Priority queue is empty")
            return

        print("Priority Queue:")
        for priority, item in sorted(self.queue):
            print("Item:", item, "Priority:", -priority)


# Example usage
pq = PriorityQueue()

pq.enqueue("Task A", 2)
pq.enqueue("Task B", 5)
pq.enqueue("Task C", 1)
pq.enqueue("Task D", 4)

pq.display()

print("\nHighest priority item:", pq.dequeue())

print("\nAfter dequeue:")
pq.display()
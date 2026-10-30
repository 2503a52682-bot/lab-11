from collections import deque


class CafeteriaQueue:
    """Manage cafeteria orders using a FIFO queue."""

    def __init__(self):
        """Initialize an empty cafeteria order queue."""
        self.orders = deque()

    def add_order(self, student, food):
        """Add a new food order to the rear of the queue.

        Args:
            student (str): Name of the student.
            food (str): Food item ordered by the student.
        """
        order = {
            "student": student,
            "food": food
        }

        self.orders.append(order)

    def serve_order(self):
        """Serve and remove the first order in the queue.

        Returns:
            dict: The order served.

        Raises:
            IndexError: If there are no orders.
        """
        if not self.orders:
            raise IndexError("No orders in the queue")

        return self.orders.popleft()

    def display_orders(self):
        """Display all pending cafeteria orders."""
        if not self.orders:
            print("No pending orders.")
            return

        print("Pending Orders:")

        for order in self.orders:
            print(
                "Student:",
                order["student"],
                "| Food:",
                order["food"]
            )


# Example usage
cafeteria = CafeteriaQueue()

# Add student orders
cafeteria.add_order("Pramod", "Burger")
cafeteria.add_order("Rahul", "Pizza")
cafeteria.add_order("Kiran", "Biryani")

# Display pending orders
cafeteria.display_orders()

# Serve the first order
served = cafeteria.serve_order()

print("\nServed Order:")
print("Student:", served["student"])
print("Food:", served["food"])

# Display remaining orders
print("\nRemaining Orders:")
cafeteria.display_orders()
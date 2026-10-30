from collections import deque


class OrderQueue:
    """Manage customer orders using a FIFO queue."""

    def __init__(self):
        """Initialize an empty order queue."""
        self.orders = deque()

    def add_order(self, order_id, customer, product):
        """Add a new order to the queue.

        Args:
            order_id (int): Unique ID of the order.
            customer (str): Name of the customer.
            product (str): Product ordered by the customer.
        """
        order = {
            "order_id": order_id,
            "customer": customer,
            "product": product
        }

        self.orders.append(order)

    def process_order(self):
        """Process and remove the first order from the queue.

        Returns:
            dict: The order that was processed.

        Raises:
            IndexError: If there are no orders.
        """
        if not self.orders:
            raise IndexError("No orders available")

        return self.orders.popleft()

    def display_orders(self):
        """Display all pending orders."""
        if not self.orders:
            print("No pending orders.")
            return

        print("Pending Orders:")

        for order in self.orders:
            print(
                "Order ID:", order["order_id"],
                "| Customer:", order["customer"],
                "| Product:", order["product"]
            )


# Example usage
order_queue = OrderQueue()

# Add orders
order_queue.add_order(101, "Pramod", "Laptop")
order_queue.add_order(102, "Rahul", "Headphones")
order_queue.add_order(103, "Kiran", "Smartphone")

# Display orders
order_queue.display_orders()

# Process the first order
processed = order_queue.process_order()

print("\nProcessed Order:")
print("Order ID:", processed["order_id"])
print("Customer:", processed["customer"])
print("Product:", processed["product"])

# Display remaining orders
print("\nRemaining Orders:")
order_queue.display_orders()
class Products:
    total_amount = 0
    _id_counter = 0

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with a name, price, and quantity."""
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise TypeError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Quantity must be a non-negative integer")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.id = Products._id_counter

        Products.total_amount += quantity
        Products._id_counter += 1

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets a new quantity for the product, deactivates if zero."""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        Products.total_amount += quantity - self.quantity
        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Processes the purchase of a given quantity of the product."""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("You cannot buy 0 or a negative amount!")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available!")

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
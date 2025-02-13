class Products:
    total_amount = 0
    _id_counter = 0

    def __init__(self, name: str, price: float, quantity: int):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.id = Products._id_counter

        Products.total_amount += quantity
        Products._id_counter += 1

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        Products.total_amount += quantity - self.quantity
        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("You cannot buy 0 or a negative amount!")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available!")

        self.quantity -= quantity
        Products.total_amount -= quantity

        return quantity * self.price

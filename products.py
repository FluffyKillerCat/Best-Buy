class Products:
    total_amount = 0
    def __init__(self, name, price, quantity):
        if len(name.strip()) == 0:
            raise NameError("Sorry, name can not be empty")

        if price < 0:
            raise ValueError("Price can not be negative")
        if quantity < 0:
            raise ValueError("Quantity can not be negative")


        if quantity == 0:
            self.active = False
        else:
            self.active = True
            Products.total_amount += quantity
            self.quantity = quantity

        self.name = name
        self.price = price


    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity >= 0:
            if quantity < self.quantity:
                Products.total_amount -= quantity
                self.quantity = quantity
            else:
                Products.total_amount += quantity
                self.quantity = quantity
        else:
            raise ValueError("Quantity can not be negative")

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        print(f"Name:{self.name}, Price:{self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("You can not by 0 or negative amount!!!")
        self.quantity -= quantity
        Products.total_amount -= quantity
        return float(quantity * self.price)


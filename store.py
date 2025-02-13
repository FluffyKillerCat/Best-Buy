from itertools import product
from typing import List
class Store:

    def __init__(self, products):
        self.total_products = []
        for product in products:
            self.total_products.append(product)

    def add_product(self, name):
        self.total_products.append(name)

    def remove_product(self, name):
        self.total_products.remove(name)
    def get_total_quantity(self) -> int:
        total = 0
        for name in self.total_products:
            total += name.quantity
        return total
    def get_all_products(self) -> List:
        return [product for product in self.total_products if product.active == True]

    def order(self, shopping_list) -> float:
        total_price = 0
        for name, quantity in shopping_list:
            if quantity < name.quantity:
                total_price += name.price * quantity
            else:
                raise ValueError(f"We dont have {quantity} for {name.name}")
        return float(total_price)





from typing import List

class Store:

    def __init__(self, products):
        self.total_products = []
        for _product in products:
            self.total_products.append(_product)

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
        return [_product for _product in self.total_products if _product.active == True]

    def order(self, shopping_list) -> float:
        total_price = 0
        for name, quantity in shopping_list:
            for _product in self.total_products:
                if _product.name == name:






                    total_price += _product.buy(quantity)



        return float(total_price)





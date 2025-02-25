from typing import List
from products import Products

class Store:
    def __init__(self, products: List[Products]):
        """
        Initializes the store with a list of products.
        :param products: List of Products to add to the store.
        """
        if not isinstance(products, list) or not all(isinstance(p, Products) for p in products):
            raise TypeError("products must be a list of Products instances")
        self.total_products = products

    def add_product(self, product: Products):
        """
        Adds a product to the store.
        :param product: Product instance to add.
        """
        if not isinstance(product, Products):
            raise TypeError("product must be an instance of Products")
        self.total_products.append(product)

    def remove_product(self, product: Products):
        """
        Removes a product from the store if it exists.
        :param product: Product instance to remove.
        """
        if not isinstance(product, Products):
            raise TypeError("product must be an instance of Products")
        if product not in self.total_products:
            raise ValueError("Product does not exist in the store")
        self.total_products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        """
        return sum(product.quantity for product in self.total_products)

    def get_all_products(self) -> List[Products]:
        """
        Returns a list of all active products in the store.
        """
        return [product for product in self.total_products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Processes an order based on a shopping list.
        :param shopping_list: List of tuples containing (product_name, quantity)
        :return: Total price of the order.
        """
        total_price = 0.0
        for name, quantity in shopping_list:
            for product in self.total_products:
                if product.name == name:
                    total_price += product.buy(quantity)
        return total_price

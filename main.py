import products
from store import Store
product_list = [products.Products("MacBook Air M2", price=1450, quantity=100),
                products.Products("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Products("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
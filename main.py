import products
import store
from typing import List, Tuple


def initialize_store() -> store.Store:
    product_list = [
        products.Products("MacBook Air M2", price=1450, quantity=100),
        products.Products("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Products("Google Pixel 7", price=500, quantity=250),
    ]
    return store.Store(product_list)


def list_all_products(store_instance: store.Store) -> None:
    active_products = store_instance.get_all_products()
    if not active_products:
        print("Empty Store!!!")
        return
    for idx, product in enumerate(active_products, start=1):
        print(f"{idx}. {product.show()}")


def get_total_amount(store_instance: store.Store) -> int:
    return store_instance.get_total_quantity()


def get_user_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def order(store_instance: store.Store) -> None:
    total_price = 0.0
    while True:
        active_products = store_instance.get_all_products()
        if not active_products:
            print("No active products available.")
            break

        print("\nCurrent available products:")
        list_all_products(store_instance)

        user_choice = get_user_int("Enter product # (press 0 to finish order): ")
        if user_choice == 0:
            break

        if 1 <= user_choice <= len(active_products):
            product = active_products[user_choice - 1]
            quantity = get_user_int(f"Enter quantity (max {product.quantity}): ")
            if 1 <= quantity <= product.quantity:
                try:
                    price = product.buy(quantity)
                    total_price += price
                    print(f"Added {quantity} of {product.name} to order. Price: {price}\n")
                except ValueError as e:
                    print(e)
            else:
                print(f"Please enter a quantity between 1 and {product.quantity}.")
        else:
            print("Invalid choice! Please select a valid product number.")
    print(f"\nTotal order price: {total_price}")


def start(store_instance: store.Store) -> None:
    menu = (
        "\n1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit\n"
    )
    while True:
        print(menu)
        user_option = input("Please choose an option: ").strip()
        match user_option:
            case "1":
                list_all_products(store_instance)
            case "2":
                print(f"Total amount in store: {get_total_amount(store_instance)}")
            case "3":
                order(store_instance)
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option! Please choose from the menu.")


if __name__ == "__main__":
    best_buy = initialize_store()
    start(best_buy)

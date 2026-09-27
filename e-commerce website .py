# E-Commerce Website - Python Program

products = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Smartphone", "price": 25000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1500},
    5: {"name": "Mouse", "price": 800}
}

cart = {}


def display_products():
    print("\n========== PRODUCTS ==========")

    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} - "
            f"Rs.{product['price']}"
        )


def add_to_cart():
    display_products()

    try:
        product_id = int(input("\nEnter product ID: "))
        quantity = int(input("Enter quantity: "))

        if product_id not in products:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Invalid quantity.")
            return

        cart[product_id] = cart.get(product_id, 0) + quantity

        print("Product added to cart successfully!")

    except ValueError:
        print("Please enter valid numbers.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        amount = product["price"] * quantity

        print(
            f"{product['name']} x {quantity} "
            f"= Rs.{amount}"
        )

        total += amount

    print("-------------------------------")
    print(f"Total Amount: Rs.{total}")


def checkout():
    if not cart:
        print("\nYour cart is empty.")
        return

    total = 0

    print("\n========== CHECKOUT ==========")

    for product_id, quantity in cart.items():
        product = products[product_id]
        total += product["price"] * quantity

    print(f"Total Amount: Rs.{total}")

    print("\nPayment Methods:")
    print("1. Cash on Delivery")
    print("2. Online Payment")

    choice = input("Select payment method: ")

    if choice == "1":
        print("Payment Method: Cash on Delivery")
    elif choice == "2":
        print("Payment Method: Online Payment")
    else:
        print("Invalid payment method.")
        return

    print("\nOrder placed successfully!")
    print("Thank you for shopping with us.")

    cart.clear()


while True:

    print("\n================================")
    print("       E-COMMERCE WEBSITE")
    print("================================")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")

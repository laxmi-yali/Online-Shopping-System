
products = {
    "Laptop": 45000,
    "Mobile": 15000,
    "Headphones": 1000,
    "Keyboard": 800,
    "Mouse": 500
}

cart = {}

while True:

    print("\n===== ONLINE SHOPPING =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for name, price in products.items():
            print(name, "- Rs.", price)

    elif choice == "2":
        name = input("Enter product name: ")

        if name in products:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                cart[name] = cart.get(name, 0) + quantity
                print("Product added!")
            else:
                print("Enter a valid quantity.")
        else:
            print("Product not available!")

    elif choice == "3":
        total = 0

        for name, quantity in cart.items():
            price = products[name] * quantity
            print(name, "x", quantity, "=", price)
            total += price

        print("Total Amount: Rs.", total)

    elif choice == "4":
        name = input("Enter product to remove: ")

        if name in cart:
            del cart[name]
            print("Product removed!")
        else:
            print("Product not in cart!")

    elif choice == "5":
        total = sum(
            products[name] * quantity
            for name, quantity in cart.items()
        )

        print("===== FINAL BILL =====")
        for name, quantity in cart.items():
            print(name, "x", quantity,
                  "=", products[name] * quantity)

        print("Total: Rs.", total)
        print("Thank you for shopping!")
        cart.clear()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

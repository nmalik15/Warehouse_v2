import os

# Initialize account balance and warehouse inventory
account_balance = 0
inventory = {}
operations = []

def clear_screen():
    if (os.name) == "nt":
        os.system('cls')
    else:
        os.system('clear')

def key_press():
    input("Press ENTER to continue...")

def manage_balance():
    """Add or subtract amount from account balance."""
    global account_balance, operations
    print("\nDo you want to: ")
    print("\t1. Add to account balance ")
    print("\t2. Subtract from account balance ")
    choice = input("Enter choice: ")
    if choice == "1":
        amount = float(input("Please enter amount to add to account balance: "))
        account_balance += amount
        operations.append(("Balance", amount))
        print(f"\nNEW ACCOUNT BALANCE: {account_balance}")
        key_press()
    elif choice == "2":
        amount = float(input("Please enter amount to subtract from account balance: "))
        account_balance -= amount
        operations.append(("Balance", -amount))
        print(f"\nNEW ACCOUNT BALANCE: {account_balance}")
        key_press()

    else:
        print("\nERROR! INVALID COMMAND. TRY AGAIN.")
        key_press()


def record_sale():
    """Record a sale."""
    global account_balance, inventory, operations
    product = input("Enter product name: ")
    if product in inventory:
        price = inventory[product][1]
        quantity = int(input("Enter product quantity: "))
        if quantity <= inventory[product][0]:
            total_sale = price * quantity
            account_balance += total_sale
            inventory[product] = (inventory[product][0] - quantity, price)
            if inventory[product][0] == 0:
                del inventory[product]
            operations.append(("Sale", (product, quantity, price, total_sale)))
            print(f"Sale recorded. New account balance: {account_balance}")
            key_press()
        else:
            print(f"Insufficient quantity of {product} in the inventory.")
            key_press()
    else:
        print(f"{product} is not available in the inventory.")
        key_press()

def record_purchase():
    """Record a purchase."""
    global account_balance, inventory, operations
    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    total_cost = price * quantity
    if total_cost <= account_balance:
        account_balance -= total_cost
        if product in inventory:
            inventory[product] = (inventory[product][0] + quantity, price)
        else:
            inventory[product] = (quantity, price)
        operations.append(("Purchase", (product, quantity, price, total_cost)))
        print(f"Purchase recorded. New account balance: {account_balance}")
        key_press()
    else:
        print("ERROR! INSUFFICIENT BALANCE FOR THIS PURCHASE!")
        key_press()

def display_account_balance():
    """Display current account balance."""
    global account_balance
    print(f"\nCurrent account balance: {account_balance}")
    key_press()

def display_inventory():
    """Display warehouse inventory."""
    global inventory
    print("Warehouse Inventory:")
    for product, (quantity, price) in inventory.items():
        print(f"{product}:\n\tStock: {quantity} \n\tPrice: {price}")
    key_press()

def display_product_status():
    """Display product status in warehouse."""
    global inventory
    product = input("Enter product name: ")
    if product in inventory:
        quantity, price = inventory[product]
        print(f"{product}:\n\tStock: {quantity} \n\tPrice: {price}")
        key_press()
    else:
        print(f"Error! {product} is not in the warehouse.".upper())
        key_press()

def review_operations():
    """Review recorded operations."""
    global operations
    start = input("Enter starting index (leave blank to start from the beginning): ")
    end = input("Enter ending index (leave blank to go until the end): ")
    if not start:
        start = 0
    else:
        start = int(start)
    if not end:
        end = len(operations)
    else:
        end = int(end)
    if start < 0 or end > len(operations) or start >= end:
        print("Invalid range.")
        key_press()
    else:
        for i in range(start, end):
            operation, details = operations[i]
            if operation == "Balance":
                amount = details
                print(f"{i+1}. Balance changed by {amount}")
            elif operation == "Sale":
                product, quantity, price, total_sale = details
                print(f"{i+1}. Sold {quantity} units of {product} for {total_sale}")
            elif operation == "Purchase":
                product, quantity, price, total_cost = details
                print(f"{i+1}. Purchased {quantity} units of {product} for {total_cost}")
        key_press()

# Main program loop
while True:
    clear_screen()
    print("*** >>  WAREHOUSE ACCOUNTING << ***")
    print("\nPlease select the number for action:")
    print("\t1. Balance - Add or subtract amount from account")
    print("\t2. Sale - Record a sale")
    print("\t3. Purchase - Record a purchase")
    print("\t4. Account - Display account balance")
    print("\t5. List - Display warehouse inventory")
    print("\t6. Warehouse - Display product status in warehouse")
    print("\t7. Review - Review recorded operations")
    print("\t8. END - Terminate program")

    command = input("\nEnter choice: ")

    if command == "1":
        manage_balance()
            
    elif command == "2":
        record_sale()

    elif command == "3":
        record_purchase()

    elif command == "4":
        display_account_balance()

    elif command == "5":
        display_inventory()

    elif command == "6":
        display_product_status()

    elif command == "7":
        review_operations()

    elif command == "8":
        print("Terminating program...")
        break

    else:
        print("\n ERROR! INVALID COMMAND! PLEASE TRY AGAIN!")
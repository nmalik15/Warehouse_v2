# Initialize account balance and warehouse inventory
account_balance = 0
inventory = {}
operations = []

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
    elif choice == "2":
        amount = float(input("Please enter amount to subtract from account balance: "))
        account_balance -= amount
        operations.append(("Balance", -amount))
        print(f"\nNEW ACCOUNT BALANCE: {account_balance}")
    else:
        print("\nERROR! INVALID COMMAND. TRY AGAIN.")

def record_sale():
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
        else:
            print(f"Insufficient quantity of {product} in the inventory.")
    else:
        print(f"{product} is not available in the inventory.")

def record_purchase():
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
    else:
        print("ERROR! INSUFFICIENT BALANCE FOR THIS PURCHASE!")

def display_account_balance():
    global account_balance
    print(f"\nCurrent account balance: {account_balance}")

def display_inventory():
    """Display warehouse inventory."""
    global inventory
    print("Warehouse Inventory:")
    for product, (quantity, price) in inventory.items():
        print(f"{product}:\n\tStock: {quantity} \n\tPrice: {price}")

# Main program loop
while True:
    print("\n*** >>  WAREHOUSE ACCOUNTING << ***")
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
        product = input("Enter product name: ")
        if product in inventory:
            # quantity = inventory[product]
            print(f"{product}:\n\tStock: {quantity} \n\tPrice: {price}")
        else:
            print(f"Error! {product} is not in the warehouse.".upper())

    elif command == "7":
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

    elif command == "8":
        print("Terminating program...")
        break

    else:
        print("\n ERROR! INVALID COMMAND! PLEASE TRY AGAIN!")
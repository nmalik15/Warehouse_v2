from functions import clear_screen, key_press, save_data, load_data, manage_balance, record_sale, record_purchase, display_account_balance, display_inventory, display_product_status, review_operations

# Main program loop
load_data()
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
        save_data()
        print("Saving data...\n")
        print("Terminating program...")
        break

    else:
        print("\n ERROR! INVALID COMMAND! PLEASE TRY AGAIN!")
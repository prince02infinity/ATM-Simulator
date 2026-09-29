
# Importing functions from our modules

from authentication import verify_pin
from account import check_balance, deposit_money, withdraw_money
from transactions import add_transaction, show_mini_statement
from pin_management import change_pin
from menu import display_menu


# Initial account details

balance = 80000
pin = "1185"
history = []


# Login section

print("================================")
print("       WELCOME TO ATM")
print("================================")

login_successful = verify_pin(pin)

if login_successful:

    # Main ATM menu

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance, amount = deposit_money(balance)

            if amount > 0:
                add_transaction(history, "Deposit", amount, balance)

        elif choice == "3":
            balance, amount = withdraw_money(balance)

            if amount > 0:
                add_transaction(history, "Withdrawal", amount, balance)

        elif choice == "4":
            show_mini_statement(history)

        elif choice == "5":
            pin = change_pin(pin)

        elif choice == "6":
            print("\nThank you for using our ATM!")
            print("Have a nice day!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")

else:
    print("\nPlease contact your bank for assistance.")
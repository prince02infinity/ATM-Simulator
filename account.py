
def check_balance(balance):
    print("\nYour current balance is Rs.", balance)


def deposit_money(balance):
    try:
        amount = int(input("Enter the amount to deposit: Rs. "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return balance, 0

        else:
            balance = balance + amount
            print("Money deposited successfully!")
            print("Updated balance: Rs.", balance)

            return balance, amount

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance, 0


def withdraw_money(balance):
    try:
        amount = int(input("Enter the amount to withdraw: Rs. "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return balance, 0

        elif amount % 100 != 0:
            print("Please enter an amount in multiples of 100.")
            return balance, 0

        elif amount > balance:
            print("Insufficient balance!")
            return balance, 0

        else:
            balance = balance - amount
            print("Please collect your cash.")
            print("Updated balance: Rs.", balance)

            return balance, amount

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return balance, 0
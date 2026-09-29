
def verify_pin(correct_pin):
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if entered_pin == correct_pin:
            print("\nLogin successful!")
            return True

        attempts -= 1

        if attempts > 0:
            print("Incorrect PIN. Please try again.")
            print("Attempts remaining:", attempts)
        else:
            print("\nYou have entered the wrong PIN 3 times.")
            print("Your access has been blocked.")

    return False



def change_pin(current_pin):
    entered_pin = input("Enter your current PIN: ")

    if entered_pin != current_pin:
        print("Incorrect current PIN. PIN change failed.")
        return current_pin

    new_pin = input("Enter your new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return current_pin

    confirm_pin = input("Confirm your new PIN: ")

    if new_pin == confirm_pin:
        print("PIN changed successfully!")
        return new_pin

    else:
        print("PIN confirmation does not match.")
        print("Your old PIN remains unchanged.")
        return current_pin
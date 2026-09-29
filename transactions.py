
def add_transaction(history, transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance": balance
    }

    history.append(transaction)


def show_mini_statement(history):
    print("\n========== MINI STATEMENT ==========")

    if len(history) == 0:
        print("No transactions found.")

    else:
        for transaction in history:
            print("Transaction:", transaction["type"])
            print("Amount: Rs.", transaction["amount"])
            print("Balance: Rs.", transaction["balance"])
            print("-----------------------------------")

    print("====================================")
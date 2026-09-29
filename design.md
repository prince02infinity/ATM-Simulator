# Project Design

## 1. Introduction
The ATM Simulator is a simple Python project that performs basic ATM operations through a console. It allows users to check their balance, deposit money, withdraw money, view transaction history, and change their PIN.

## 2. Program Structure
The project is divided into different Python files. Each file is responsible for a specific task.

- `main.py` – Runs the main program and connects all the modules.
- `authentication.py` – Checks the user's PIN.
- `menu.py` – Displays the ATM menu.
- `account.py` – Handles balance checking, deposits, and withdrawals.
- `transactions.py` – Stores and displays transaction history.
- `pin_management.py` – Allows the user to change their PIN.

## 3. Working of the Program
1. The program displays a welcome message.
2. The user enters their PIN.
3. If the PIN is correct, the ATM menu is displayed.
4. The user selects an operation.
5. The program performs the selected operation.
6. The menu appears again so the user can choose another operation.
7. The program ends when the user selects Exit.

## 4. Conclusion
The project uses basic Python concepts such as variables, functions, loops, conditional statements, lists, dictionaries, and modules. It helped me understand how different parts of a program work together.s
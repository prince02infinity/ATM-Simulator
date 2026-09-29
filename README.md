# ATM Simulator Using Python

### A Beginner-Friendly Console-Based Banking Application

---

## 1. Project Overview

The ATM Simulator is a Python-based console application developed to demonstrate the basic operations of an Automated Teller Machine (ATM). It allows a user to access a sample bank account through PIN verification and perform common banking activities such as checking the account balance, depositing money, withdrawing cash, viewing transaction history, and changing the PIN.

The main purpose of this project is to understand how fundamental Python programming concepts can be combined to build a simple application based on a real-world system.

The program follows a menu-driven approach, where the user selects an operation from the displayed options. Each operation is handled through a separate function, making the code easier to read, understand, and maintain.

Basic security and input validation are also included to make the program more reliable. For example, the user gets a limited number of login attempts, invalid amounts are rejected, and withdrawals are allowed only when sufficient balance is available.

This project is developed as a beginner-level academic project for understanding Python programming through practical implementation.

---

## 2. Project Information

| Detail                  | Description                 |
| ----------------------- | --------------------------- |
| Project Title           | ATM Simulator Using Python  |
| Programming Language    | Python                      |
| Project Type            | Console-Based Application   |
| Academic Level          | First-Year B.Tech           |
| Course Code             | CSE1021                     |
| Application Domain      | Banking Simulation          |
| Main File               | `main.py`                   |
| Documentation File      | `README.md`                 |
| Initial Account Balance | Rs. 88500                    |
| Default PIN             | 1185                       |
| Data Storage            | Temporary in-memory storage |

---

## 3. Problem Statement

Automated Teller Machines are commonly used for basic banking operations such as cash withdrawal, deposits, and balance enquiries. Understanding how these operations work can help beginners connect programming concepts with practical applications.

The objective of this project is to develop a simple ATM simulation using Python that demonstrates the working of these operations without requiring a real banking system or database.

The program provides a basic interface through which a user can log in, select an operation, and view the result. It also handles common input errors and restricts access after repeated incorrect PIN entries.

---

## 4. Objectives

The main objectives of this project are:

1. To understand the fundamentals of Python programming through practical implementation.
2. To develop a menu-driven application using conditional statements and loops.
3. To understand how functions can divide a program into smaller, manageable parts.
4. To implement basic PIN verification with limited login attempts.
5. To perform simple account operations such as deposits and withdrawals.
6. To maintain a transaction history using a Python list.
7. To apply input validation and exception handling.
8. To improve logical thinking and problem-solving skills.
9. To understand how a simple real-world application can be developed using basic programming concepts.

---

## 5. Features of the Application

### 5.1 PIN Verification

The program asks the user to enter a four-digit PIN before displaying the ATM menu. Access is granted only when the entered PIN matches the stored PIN.

### 5.2 Limited Login Attempts

The user is given three attempts to enter the correct PIN. If all attempts fail, the program displays a message indicating that the account is temporarily locked and ends the session.

### 5.3 Balance Enquiry

The user can check the current account balance at any time after successful login.

### 5.4 Cash Withdrawal

The withdrawal feature allows the user to withdraw money from the account.

Before processing a withdrawal, the program checks that:

* The entered amount is a valid number.
* The amount is greater than zero.
* Sufficient balance is available.
* The withdrawal amount is a multiple of Rs. 100.

If all conditions are satisfied, the amount is deducted from the account balance and the transaction is recorded.

### 5.5 Cash Deposit

The user can deposit money into the account by entering the desired amount.

The program accepts positive whole-number amounts. After a successful deposit, the balance is updated and the transaction is added to the transaction history.

### 5.6 Mini Statement

The mini statement displays the transactions performed during the current program session, along with the current account balance.

If no transactions have been performed, the program displays a message indicating that no transaction records are available.

### 5.7 Change PIN

The user can change the existing PIN by providing the current PIN and entering a new four-digit PIN.

The program asks the user to confirm the new PIN before updating it. If the two entries do not match, the PIN remains unchanged.

### 5.8 Input Validation

The program handles common input errors, including:

* Entering letters instead of numbers for monetary amounts.
* Entering zero or negative amounts.
* Attempting to withdraw more money than the available balance.
* Entering a withdrawal amount that is not a multiple of Rs. 100.
* Selecting an invalid menu option.

These checks help prevent incorrect operations and make the program easier to use.

### 5.9 Exit Option

The user can exit the application by selecting the Exit option from the ATM menu. A thank-you message is displayed before the program terminates.

---

## 6. Technologies and Concepts Used

### 6.1 Technology

**Python:** Python is used as the main programming language because its syntax is simple and suitable for beginners.

**Visual Studio Code:** Used as the development environment for writing and running the program.

**Command-Line Interface:** The application interacts with the user through text-based input and output.

### 6.2 Python Concepts Applied

| Concept                | Application in the Project                           |
| ---------------------- | ---------------------------------------------------- |
| Variables              | Store account balance and PIN                        |
| Data Types             | Use integers, strings, and lists                     |
| Conditional Statements | Check PINs, menu choices, and transaction conditions |
| Loops                  | Repeat login attempts and display the ATM menu       |
| Functions              | Separate different ATM operations                    |
| Lists                  | Store transaction history                            |
| User Input             | Accept PINs, amounts, and menu selections            |
| Exception Handling     | Handle invalid numerical input using `try-except`    |
| Global Variables       | Allow functions to update the shared balance and PIN |
| String Operations      | Validate the new PIN and display transaction details |

---

## 7. System Requirements

### 7.1 Hardware Requirements

The project can run on a basic computer with:

* A desktop computer or laptop.
* A keyboard for entering information.
* Sufficient memory to run Python and a code editor.

No special hardware is required.

### 7.2 Software Requirements

* Python installed on the system.
* Visual Studio Code or any suitable Python editor.
* A terminal or command prompt to execute the program.

The project uses Python's built-in features and does not require any third-party libraries.

---

## 8. Project Structure

The project is organized into a simple folder structure:

```text
ATM_Simulator Project/
│
├── main.py
│
└── README.md
```

### File Description

**`main.py`**

This is the main Python program. It contains the account details, PIN verification, ATM menu, banking functions, transaction history, and the main program execution.

**`README.md`**

This file contains the project overview, objectives, features, requirements, instructions for execution, testing details, limitations, and conclusion.

---

## 9. Working of the Application

The ATM Simulator follows a simple sequence of operations.

### Step 1: Program Initialization

When the program starts, the account balance is initialized to Rs. 5000, the default PIN is set to 1234, and an empty list is created to store transactions.

### Step 2: User Authentication

The user is asked to enter the PIN. The program compares the entered PIN with the stored PIN.

If the PIN is correct, the user is allowed to continue. Otherwise, the number of remaining attempts is reduced.

### Step 3: Displaying the ATM Menu

After successful login, the program displays the following options:

```text
====================================
              ATM MENU
====================================
1. Balance Enquiry
2. Cash Withdrawal
3. Cash Deposit
4. Mini Statement
5. Change PIN
6. Exit
====================================
```

### Step 4: Selecting an Operation

The user enters a choice between 1 and 6. The program calls the corresponding function to perform the selected operation.

### Step 5: Updating Account Information

When a deposit or withdrawal is completed successfully, the account balance is updated and the transaction is added to the transaction history.

### Step 6: Returning to the Menu

After an operation is completed, the program returns to the ATM menu so that the user can perform another operation.

### Step 7: Exiting the Program

When the user selects option 6, the program displays a thank-you message and terminates.

---

## 10. Algorithm

1. Start the program.
2. Initialize the account balance to Rs. 5000.
3. Set the default PIN to 1234.
4. Create an empty list for storing transactions.
5. Display the welcome message.
6. Ask the user to enter the PIN.
7. Verify the entered PIN.
8. If the PIN is incorrect, reduce the remaining attempts and ask again.
9. If all three attempts fail, display the account lock message and end the program.
10. If the PIN is correct, display the ATM menu.
11. Accept the user's menu choice.
12. Perform the selected operation:

    * Display the balance.
    * Withdraw money after checking the conditions.
    * Deposit money after validating the amount.
    * Display the mini statement.
    * Change the PIN after verification.
    * Exit the application.
13. Return to the menu after each operation unless the user chooses Exit.
14. End the program.

---

## 11. Testing and Validation

The program was tested using different inputs to check whether the operations work as expected.

| Test Case                 | Input                       | Expected Result                |
| ------------------------- | --------------------------- | ------------------------------ |
| Correct PIN               | 1234                        | Login successful               |
| Incorrect PIN             | 0000                        | Incorrect PIN message          |
| Three incorrect attempts  | Three wrong PIN entries     | Account temporarily locked     |
| Balance enquiry           | Select option 1             | Displays current balance       |
| Valid deposit             | 1000                        | Balance increases by Rs. 1000  |
| Negative deposit          | -500                        | Deposit rejected               |
| Zero deposit              | 0                           | Deposit rejected               |
| Invalid deposit input     | abc                         | Error message displayed        |
| Valid withdrawal          | 500                         | Balance decreases by Rs. 500   |
| Insufficient balance      | Amount greater than balance | Withdrawal rejected            |
| Invalid withdrawal amount | 250                         | Withdrawal rejected            |
| Mini statement            | Select option 4             | Displays recorded transactions |
| Change PIN                | Enter valid matching PINs   | PIN updated successfully       |
| Mismatched new PIN        | Different confirmation PIN  | PIN change rejected            |
| Invalid menu choice       | 9                           | Invalid choice message         |
| Exit                      | Select option 6             | Thank-you message displayed    |

The test cases cover normal operations as well as common incorrect inputs.

---

## 12. Sample Execution

The following example illustrates a typical program session.

```text
====================================
       WELCOME TO PYTHON ATM
====================================

Please insert your card.
Thank you for choosing our ATM!

Enter your 4-digit PIN: 1234

Login successful!

You can now access your account.

====================================
              ATM MENU
====================================
1. Balance Enquiry
2. Cash Withdrawal
3. Cash Deposit
4. Mini Statement
5. Change PIN
6. Exit
====================================

Enter your choice (1-6): 1

----------- BALANCE ENQUIRY -----------
Your current balance is: Rs. 5000
---------------------------------------
```

This output is an example of the balance enquiry operation. The actual balance displayed will depend on the transactions performed during the session.

---

## 13. Limitations

Although the project demonstrates the basic working of an ATM, it has some limitations:

1. The account balance is stored in a variable and is not saved permanently.
2. Transaction history is stored in a Python list and is lost when the program ends.
3. The PIN is stored directly in the source code.
4. The application supports only one sample account.
5. There is no database connection.
6. The program does not connect to any real banking service.
7. The account lock is limited to the current program execution.
8. The application is intended for learning and demonstration purposes only.

These limitations are acceptable for a beginner-level console application and provide opportunities for future improvement.

---

## 14. Future Scope

The project can be improved further by adding more features as programming knowledge increases.

Possible improvements include:

* Saving account information permanently using file handling.
* Using a database to store account details and transactions.
* Supporting multiple user accounts.
* Adding a graphical user interface.
* Improving PIN security.
* Generating downloadable transaction statements.
* Adding transaction dates and times.
* Introducing separate account types and account management features.

These improvements could make the application more realistic while providing opportunities to learn additional programming concepts.

---

## 15. Learning Outcomes

Through the development of this project, I gained practical experience in:

1. Writing and executing Python programs.
2. Using variables and different data types.
3. Applying conditional statements and loops.
4. Creating and calling functions.
5. Managing data using lists.
6. Accepting user input and displaying output.
7. Handling invalid inputs using exception handling.
8. Breaking a larger problem into smaller tasks.
9. Testing a program with different input conditions.
10. Understanding how programming concepts are used in a practical application.

The project also helped me improve my confidence in writing, debugging, and explaining Python code.

---

## 16. Conclusion

The ATM Simulator is a beginner-friendly Python project that demonstrates how basic programming concepts can be used to develop a simple banking application.

It provides essential ATM operations such as PIN verification, balance enquiry, cash deposits, withdrawals, transaction history, and PIN changes. The program also includes basic input validation and limited login attempts to make its operation more reliable.

While developing this project, I learned how to use variables, conditional statements, loops, functions, lists, and exception handling in a practical situation. I also understood the importance of testing a program with different inputs and handling errors properly.

Overall, this project gave me valuable hands-on experience with Python and helped me understand how a simple real-world application can be developed step by step.

---

## 17. Author

**Project:** ATM Simulator Using Python
**Course:** CSE1021
**Academic Level:** First-Year B.Tech
**Institution:** VIT Bhopal University

**Developed as part of the introductory Python programming coursework.**

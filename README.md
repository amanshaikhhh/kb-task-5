# kb-task-5
Password Strength Checker (Python CLI Utility)
Project Overview
This Password Strength Checker is a Python command-line utility that helps users evaluate the strength of passwords based on multiple security criteria. The script validates whether the password meets common standards for strong passwords—minimum length, use of uppercase letters, digits, and special characters—using both string manipulation and regex.

Features
Accepts password input from the user via the command line

Checks for:

Minimum length (8 characters)

At least one uppercase letter

At least one number

At least one special character

Uses Python’s re module for efficient regular expression-based validation

Clearly indicates whether the password is “Strong” or “Weak”

Includes sample passwords for user guidance in code comments or prompts.

How to Run
Ensure Python is installed on your device.

Save the script as password_checker.py.

Open a terminal, navigate to the script’s directory, and run:

text
python password_checker.py
Follow the prompt to enter a test password, and review the feedback.

Example Usage
text
Example strong passwords: My_P@ssw0rd! | King$2025 | SecurePass1#
Example weak passwords: pass123 | password | 12345678 | ABCDEF#

Enter your password: My_P@ssw0rd!
Strong
What I Learned
Leveraged regular expressions for fast and flexible input validation

Explored password standards and the value of basic security principles

Improved user experience with clear prompts and helpful usage examples

Practiced designing CLI utilities that extend beyond theory into practical use

Potential Improvements
Add feedback for missing specific criteria (e.g., “Add a special character”)

Integrate with a password generator

Support saving validated passwords securely

Expand checks for commonly used passwords or data breaches

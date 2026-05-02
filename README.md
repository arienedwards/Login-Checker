# Login-Checker

Login Checker V1

This is verison 1 of my custom login checker that I built in Python.
It validates a username and password based on basic security rules.

Features

- Username validation:
- Must be between 7–15 characters
  
Password validation:

-Must be between 8–20 characters
-Prevents weak inputs
-Re-prompts user until valid input is entered

What I Learned

- Python basics (input, variables, conditionals)
- Using loops (`while`) to control program flow
- Basic input validation (important in cybersecurity)
- Structuring a simple security-focused script

How to Run

- Make sure Python is installed
- Run the script:

bash
python3 login_checker.py

Example Output

Enter username: user
Try Again: Username too short

Enter username: validuser
Strong Username

Enter password: 123
Try Again: Password too short

Enter password: StrongPass123!
Strong Password

Future Improvements

Require:

- At least 1 uppercase letter
- At least 1 number
- At least 1 special character
- Hide password input
- Store credentials securely (hashed)
- Add login attempt limits

Why This Matters (Cybersecurity)

Input validation is a foundational concept in cybersecurity.
Weak validation can lead to:

- brute force attacks
- injection vulnerabilities
- weak authentication systems

This project demonstrates the basics of enforcing stronger user input.

Arien Edwards



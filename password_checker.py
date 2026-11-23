
# Password Security Checker
# Project 01 - Beginner Cybersecurity Project

def check_password(password):

    # Common passwords list
    common_passwords = {
        "password",
        "password123",
        "12345678",
        "qwerty123",
        "admin123",
        "welcome123",
        "iloveyou"
    }

    # Check password characteristics
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Uppercase letter": any(c.isupper() for c in password),
        "Lowercase letter": any(c.islower() for c in password),
        "Number": any(c.isdigit() for c in password),
        "Special character": any(not c.isalnum() for c in password),
        "Not a common password": password.lower() not in common_passwords
    }

    # Display security checks
    print("\n--- Password Security Report ---")

    for check, result in checks.items():
        status = "PASS" if result else "FAIL"
        print(f"{check}: {status}")

    # Calculate score
    score = sum(checks.values())

    # Classify password
    if password.lower() in common_passwords or len(password) < 8:
        strength = "WEAK"
    elif score == 6:
        strength = "STRONG"
    else:
        strength = "MODERATE"

    # Display final result
    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 6")

    # Recommendations
    print("\n--- Recommendations ---")

    for check, result in checks.items():
        if not result:
            print("Improve:", check)

    if all(checks.values()):
        print("Good! All basic security checks passed.")

    print("\nNote: This is a basic educational checker.")
    print("It cannot guarantee password security.")


# Main program
print("================================")
print("     PASSWORD SECURITY CHECKER")
print("================================")

user_password = input("\nEnter a test password: ")

check_password(user_password)

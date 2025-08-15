import string
import secrets
import sys
from getpass import getpass
from typing import List, Tuple

MIN_LENGTH = 12
MIN_DIGITS = 4
MIN_UPPERCASE = 3
MIN_LOWERCASE = 3
MIN_SPECIAL = 2
SPECIAL_CHARACTERS = '@#$?%&*!'

def generate_password(length: int = MIN_LENGTH) -> str:
    if length < MIN_LENGTH:
        raise ValueError(f"Password length must be at least {MIN_LENGTH} characters.")
    while True:
        password_chars = (
            [secrets.choice(string.digits) for _ in range(MIN_DIGITS)] +
            [secrets.choice(string.ascii_uppercase) for _ in range(MIN_UPPERCASE)] +
            [secrets.choice(string.ascii_lowercase) for _ in range(MIN_LOWERCASE)] +
            [secrets.choice(SPECIAL_CHARACTERS) for _ in range(MIN_SPECIAL)]
        )
        all_chars = string.ascii_letters + string.digits + SPECIAL_CHARACTERS
        password_chars += [secrets.choice(all_chars) for _ in range(length - len(password_chars))]
        secrets.SystemRandom().shuffle(password_chars)
        password = ''.join(password_chars)
        if check_password_strength(password)[0]:
            return password

def check_password_strength(password: str) -> Tuple[bool, List[str]]:
    issues = []
    if len(password) < MIN_LENGTH:
        issues.append(f"Password must be at least {MIN_LENGTH} characters.")
    if sum(c.isdigit() for c in password) < MIN_DIGITS:
        issues.append(f"Password must contain at least {MIN_DIGITS} digits.")
    if sum(c.isupper() for c in password) < MIN_UPPERCASE:
        issues.append(f"Password must contain at least {MIN_UPPERCASE} uppercase letters.")
    if sum(c.islower() for c in password) < MIN_LOWERCASE:
        issues.append(f"Password must contain at least {MIN_LOWERCASE} lowercase letters.")
    if sum(c in SPECIAL_CHARACTERS for c in password) < MIN_SPECIAL:
        issues.append(f"Password must contain at least {MIN_SPECIAL} special characters ({SPECIAL_CHARACTERS}).")
    common_patterns = ['abcdef', 'qwerty', 'asdfgh', 'zxcvbn', 'password', '123456', 'letmein', 'welcome']
    for pattern in common_patterns:
        if pattern in password.lower():
            issues.append("Password should not contain common sequences or patterns.")
            break
    return (len(issues) == 0, issues)

def guidelines() -> None:
    print("\n\033[1mZ+ Password Manager: Guidelines for a Strong Password\033[0m")
    print("-" * 60)
    print(f"1. Minimum length: {MIN_LENGTH} characters")
    print(f"2. At least {MIN_DIGITS} digits")
    print(f"3. At least {MIN_UPPERCASE} uppercase letters")
    print(f"4. At least {MIN_LOWERCASE} lowercase letters")
    print(f"5. At least {MIN_SPECIAL} special characters ({SPECIAL_CHARACTERS})")
    print("6. Avoid personal names, common words, or patterns (e.g., 'qwerty').")
    print("7. Do not use easily guessable info (birthdays, phone numbers, etc.)")
    print("\nTips: Mix all character types and avoid any repetition or predictability.\n")

def get_masked_password(prompt: str = "Enter your password: ") -> str:
    return getpass(prompt)

def password_strength_cli() -> None:
    while True:
        print("\n\033[1mPassword Strength Checker\033[0m")
        password = get_masked_password()
        is_strong, issues = check_password_strength(password)
        if is_strong:
            print("\033[92mYour password is strong! Great job!\033[0m")
            break
        else:
            print("\n\033[91mYour password has the following issues:\033[0m")
            for i, issue in enumerate(issues, 1):
                print(f"{i}. {issue}")
            print("\nOptions:")
            print("  1. Try again")
            print("  2. View guidelines")
            print("  3. Get a suggested strong password")
            print("  4. Return to main menu")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == 1:
                continue
            elif choice == 2:
                guidelines()
            elif choice == 3:
                print("\n\033[94mSuggested strong password:\033[0m")
                print(generate_password())
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please select a valid option.")

def main_menu() -> None:
    print("\n\033[1mWelcome to Z+ Password Manager: Advanced Password Utility\033[0m")
    print("Safeguard your digital world with industry-standard security.\n")
    while True:
        print("\nMain Menu:")
        print("  1. View password guidelines")
        print("  2. Generate a strong password")
        print("  3. Test your password strength")
        print("  4. Exit")
        try:
            n = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if n == 1:
            guidelines()
        elif n == 2:
            print("\n\033[94mGenerated strong password:\033[0m")
            print(generate_password())
        elif n == 3:
            password_strength_cli()
        elif n == 4:
            print("Thank you for using Z+ Password Manager. Stay secure!")
            sys.exit(0)
        else:
            print("Invalid choice! Please select from the above options.")

if __name__ == "__main__":
    main_menu()

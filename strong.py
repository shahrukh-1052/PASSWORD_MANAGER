import string
import random

def generate_password():
    ssp = '@#$?%&*!'
    dgt = random.randint(1000, 9999)
    ult = ''.join(random.choices(string.ascii_uppercase, k=3))
    spl = ''.join(random.choices(ssp, k=2))
    llt = ''.join(random.choices(string.ascii_lowercase, k=3))
    lst = list(str(dgt) + ult + llt + spl)
    random.shuffle(lst)
    rst = ''.join(lst)
    return rst

def chk_pwd_strength():
    while True:
        pc = '@#$?%&*!'
        upd = input("Enter Your Password: ")
        issues = []
        if len(upd) < 12:
            issues.append("First, your password must be at least 12 characters.")
        if sum(x.isdigit() for x in upd) < 4:
            issues.append("Your password must contain at least 4 numerics.")
        if sum(x.isupper() for x in upd) < 3:
            issues.append("Your password must contain at least 3 uppercase letters.")
        if sum(x.islower() for x in upd) < 3:
            issues.append("Your password must contain at least 3 lowercase letters.")
        if sum(x in pc for x in upd) < 2:
            issues.append("Your password must contain at least 2 special characters.")

        if issues:
            print("Your password doesn't meet the following conditions:")
            for zx in issues:
                print(f"{zx}")
            
            while True:
                print("Enter '1' to try again.")
                print("Enter '2' to read the instructions for strong password generation.")
                print("Enter '3' to get a generated strong password.")
                print("Enter '4' to go to the main menu.")
                qw = int(input("Enter your choice: "))
                if qw == 1:
                    print("Please try again.")
                    break  # Breaks out of the inner while loop to try again
                elif qw == 2:
                    pwd_gdlns()
                elif qw == 3:
                    print("\nYour New Password Generated Successfully: ")
                    print(generate_password())
                elif qw == 4:
                    return
                else:
                    print("Invalid choice! Please enter a valid option.")
        else:
            print("Your password is strong enough.")
            break  # Breaks out of the outer while loop

def pwd_gdlns():
    print("\nGuidelines for Creating a Strong Password:")
    print("1. Your password must be at least 12 characters long to ensure sufficient complexity.")
    print("2. It should contain at least 4 numeric digits to add variety and make it harder to guess.")
    print("3. Include at least 2 special characters (e.g., @, #, $, %, ?, &, *, !) to increase its strength.")
    print("4. Your password must contain at least 3 uppercase letters to add diversity.")
    print("5. Include at least 3 lowercase letters to balance your password's composition.")
    print("6. Avoid using any personal names (e.g., your name, family names, or commonly used names) to prevent easy guesses.")
    print("7. Do not use common keyboard patterns or sequences like 'abcdef', 'qwerty', 'asdfgh', 'zxcvbn', or similar.")
    print("\nAdditional Tips:")
    print("- Avoid using easily identifiable personal data, such as birthdays or phone numbers.")
    print("- Mix and match letters, numbers, and symbols in unpredictable ways to create a unique password.")
    print("- Test your password to ensure it meets all the criteria and is strong enough.")

def main_menu():
    while True:
        print("\nEnter '1' to get guidelines for creating a strong password.")
        print("Enter '2' to generate a new password.")
        print("Enter '3' to test your password strength.")
        print("Enter '4' to exit.")
        n = int(input("Enter your choice: "))

        if n == 1:
            pwd_gdlns()
        elif n == 2:
            print("\nYour New Password Generated Successfully: ")
            print(generate_password())
        elif n == 3:
            chk_pwd_strength()
        elif n == 4:
            print("Exiting... Goodbye.")
            break
        else:
            print("You have entered the wrong choice! Choose your choice from the above options only.")

if __name__ == "__main__":
    main_menu()


import secrets
import string
import hashlib
import re
import uuid

# ------------------------------------------------------------
# 1. Password strength checker
# ------------------------------------------------------------
def password_strength_checker(password: str = None) -> str:
    if password is None:
        password = input('Enter a password (≥8 chars, includes number & special char): ')

    special_pattern = re.compile(r"[`~!@#$%^&*()_\-+=\[\]{};:,.<>/?]")

    if len(password) < 8:
        return "Too short (min 8 characters)"
    if not any(ch.isalpha() for ch in password):
        return "Add letters"
    if not any(ch.isdigit() for ch in password):
        return "Add at least one digit"
    if not special_pattern.search(password):
        return "Add at least one special character"
    return "Strong password ✅"


# ------------------------------------------------------------
# 2. Random password generator
# ------------------------------------------------------------
def generate_password(length: int = 12) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    all_chars = uppercase + lowercase + digits + special
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    rng = secrets.SystemRandom()
    rng.shuffle(password)

    return ''.join(password)


# ------------------------------------------------------------
# 3. SHA-256 hash
# ------------------------------------------------------------
def sha256_hash(text: str = None) -> str:
    if text is None:
        text = input('Enter a string to hash with SHA-256: ')
    return hashlib.sha256(text.encode()).hexdigest()


# ------------------------------------------------------------
# 4. XOR cipher
# ------------------------------------------------------------
def xor_cipher(text: str, key: str) -> str:
    return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

def xor_interactive():
    text = input("Enter a message to encrypt/decrypt🔒: ")
    key = input("Enter a key🔑: ")
    result = xor_cipher(text, key)
    print(f"Result: {result}")
    return result


# ------------------------------------------------------------
# 5. Simple password check with 3 attempts
# ------------------------------------------------------------
def login_simulation(password: str = "Secret123!"):
    attempts = 0
    while True:
        user_input = input("Enter password: ")
        attempts += 1
        if user_input == password:
            print("Access granted ✅")
            break
        else:
            print("Wrong password ❌")
            if attempts >= 3:
                print("Too many attempts! Locked out ⛔")
                break


# ------------------------------------------------------------
# 6. UUID generator
# ------------------------------------------------------------
def generate_uuid():
    print("Generated UUID:", str(uuid.uuid4()))

# ------------------------------------------------------------
# 7. Introduction
# ------------------------------------------------------------

def show_intro():
    print("""Issued by: \033[91mAhmed \033[0m
Date:      2026-03-20   16:08:14 UTC
Version:   1.4 
Learn, experiment, and strengthen your cybersecurity skills!
""")
banner = r"""
  _________                                    __________                       ____  __.__  __   
 /   _____/ ____   ____  __ _________   ____   \______   \_____    ______ _____|    |/ _|__|/  |_ 
 \_____  \_/ __ \_/ ___\|  |  \_  __ \_/ __ \   |     ___/\__  \  /  ___//  ___/      < |  \   __\
 /        \  ___/\  \___|  |  /|  | \/\  ___/   |    |     / __ \_\___ \ \___ \|    |  \|  ||  |  
/_______  /\___  >\___  >____/ |__|    \___  >  |____|    (____  /____  >____  >____|__ \__||__|  
        \/     \/     \/                   \/                  \/     \/     \/        \/         
"""
    # \033[92m = light green, \033[0m = reset
print("\033[92m" + banner + "\033[0m")

# ------------------------------------------------------------
# Main menu
# ------------------------------------------------------------
def main():
    while True:
        show_intro()
        print("\n=== Password Toolkit ===")
        print("1. Check password strength")
        print("2. Generate a random password")
        print("3. Compute SHA-256 hash")
        print("4. XOR encrypt/decrypt")
        print("5. Login simulation (3 attempts)")
        print("6. Generate UUID")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            print(password_strength_checker())
        elif choice == '2':
            try:
                length = int(input("Password length (default 12): ") or "12")
            except ValueError:
                length = 12
            print("Generated password:", generate_password(length))
        elif choice == '3':
            print("SHA-256 hash:", sha256_hash())
        elif choice == '4':
            xor_interactive()
        elif choice == '5':
            login_simulation()
        elif choice == '6':
            generate_uuid()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

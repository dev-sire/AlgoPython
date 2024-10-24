import string
import random
from cryptography.fernet import Fernet


def generate_password():
    """Generates a random password"""
    alphabets = list(string.ascii_letters)
    symbols = list(string.punctuation)
    digits = list(string.digits)

    no_of_alphabets = random.randint(8, 10)
    no_of_digits = random.randint(2, 4)
    no_of_symbols = random.randint(2, 4)

    final_password = random.choices(alphabets, k=no_of_alphabets) + random.choices(symbols, k=no_of_symbols)
    final_password += random.choices(digits, k=no_of_digits)
    random.shuffle(final_password)

    return "".join(final_password)


def valid_password(password):
    """Checks if the password is valid"""
    if len(password) < 8:
        return False

    alphabets = list(string.ascii_letters)
    symbols = list(string.punctuation)
    digits = list(string.digits)

    alphabets_count = 0
    symbols_count = 0
    digits_count = 0

    for i in password:
        if i in alphabets:
            alphabets_count += 1
        elif i in digits:
            digits_count += 1
        elif i in symbols:
            symbols_count += 1

    return digits_count >= 2 and symbols_count >= 1 and alphabets_count >= 5


def valid_email(email):
    return "@" in email and "." in email


def generate_new_key():
    """Generates a new key"""
    return Fernet.generate_key()


def encrypt_password(password, key):
    """Encrypt the password using the key."""
    fer = Fernet(key)
    encrypted_password = fer.encrypt(password.encode()).decode()
    return encrypted_password


def decrypt_password(encrypted_password, key):
    """Decrypts a hashed password using the key"""
    fer = Fernet(key)
    decrypted_password = fer.decrypt(encrypted_password.encode()).decode()
    return decrypted_password

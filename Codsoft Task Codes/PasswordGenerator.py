#A Password Generator
#Name : Shubham Lade
#Description : Password generator application, allowing users to specify the length and complexity of the password.
#               User Input, Generate Password, Display the Password

import string
import secrets

def generate_password(length):
    if length < 6:
        return "Error: Password length should be at least 6 characters."
    
    #define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    #combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    #one character from each category should be present
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    #rest of the password
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    #shuffle
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    print("-----A Password Generator-----")
    try:
        length = int(input("Enter the password length: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid Input: Please enter a numeric value.")

if __name__ == "__main__":
    main()
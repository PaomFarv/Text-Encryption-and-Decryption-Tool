import random
import string
from colorama import Fore, Style, init

chars = list(string.ascii_letters + string.punctuation + " " + string.digits)
key = chars.copy()
random.shuffle(key)

def text_encrypt(text):
    encrypted_text = ""
    for char in text:
        if char in chars:
            idx = chars.index(char)
            encrypted_text += key[idx]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text):
    decrypted_text = ""
    for char in text:
        if char in key:
            idx = key.index(char)
            decrypted_text += chars[idx]
        else:
            decrypted_text += char 
    return decrypted_text

print(Fore.CYAN + "-" * 60)
input(Fore.YELLOW + "Press ENTER to begin...")
print(Fore.CYAN + "-" * 60)
print(
    Fore.GREEN
    + "Which of the following tools you want to use: \n1. Text Encryptor.\n2. Text Decryptor.\n3. Exit."
)

while True:
    user_response = input(Fore.BLUE + "Insert the number of the tool you want to use: ")
    if user_response.isdigit() and 0 < int(user_response) < 4:
        user_response = int(user_response)
        pass
    else:
        print(Fore.RED + "Invalid input. Please try again.")
        continue

    if user_response == 1:
        user_text = input(Fore.YELLOW + "Enter your text to encrypt: ")
        encrypted = text_encrypt(user_text)
        print(Fore.CYAN + "Encrypted text:", Fore.MAGENTA + encrypted)

    elif user_response == 2:
        user_text_dec = input(Fore.YELLOW + "Enter encrypted text to decrypt: ")
        decrypted = decrypt_text(user_text_dec)
        print(Fore.CYAN + "Decrypted text:", Fore.MAGENTA + decrypted)

    elif user_response == 3:
        print(Fore.GREEN + "Exiting the program. Goodbye!")
        break
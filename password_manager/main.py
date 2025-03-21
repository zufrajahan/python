from cryptography.fernet import Fernet 

def generate_key():
    key = Fernet.generate_key()

    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key","rb").read()

def store_password():
    key = load_key()
    cipher = Fernet(key)
    website = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

   
    encrypted_password = cipher.encrypt(password.encode()).decode()

    with open("passwords.txt","a") as file:
        file.write(f"{website} |  {username} | {encrypted_password}\n")

    print("Password saved successfully")

def retrieve_password():
    key = load_key()
    cipher = Fernet(key)
    website = input("Enter website name to search: ")

    found = False

    with open("passwords.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if parts[0] == website:  
                decrypted_password = cipher.decrypt(parts[2].encode()).decode()
                print(f"Username: {parts[1]}")
                print(f"Password: {decrypted_password}")
                found = True
                break

    if not found:
        print("No password found for this website")


master_password = "mashugadha"

def main():

    entered_password = input("Enter master password: ")
    if(entered_password != master_password):
        print("Access denied wrong password")
        return
    print("Password Manager")
    print("1. Store new password")
    print("2. Retieve a password")
    print("3. Exit")

    choice = int(input("Enter your choice please: "))

    if choice == 1:
        print("You chose to store a password")
        store_password()
    elif choice == 2:
        print("You chose to retrieve")
        retrieve_password()
    elif choice == 3:
        print("You chose to exit... Goodbye")
    else:
        print("Invalid choice")

# generate_key()       
main()
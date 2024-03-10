import tink
from tink import aead
import sqlite3
import bcrypt

# Initialize Tink
tink.aead.register()

# Generate a keyset handle for AEAD
keyset_handle = tink.KeysetHandle.generate_new(aead.aead_key_templates.AES128_GCM)

# Initialize AEAD primitive
aead_primitive = keyset_handle.primitive(aead.Aead)

# Database initialization
conn = sqlite3.connect('user_pwd.db')
c = conn.cursor()

# Create table to store user data
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password_hash TEXT, password_salt TEXT)''')

# Function to hash password with bcrypt
def hash_password(password):
    salt =  bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(),salt)
    return hashed_password,salt

def encrypt_hash(password):
    ciphertext = aead_primitive.encrypt(plaintext=password.encode(), associated_data=b'')
    return ciphertext

def decrypt_hash(ciphertext):
    plaintext = aead_primitive.decrypt(ciphertext=ciphertext, associated_data=b'')
    return plaintext.decode()

# Function to register a new user
def register(username, password):
    hashed_password,salt = hash_password(password)

    c.execute("INSERT INTO users VALUES (?, ?, ?)", (username,encrypt_hash(hashed_password.decode('utf-8')),salt.decode('utf-8')))
    conn.commit()
    print("User registered successfully.")

# Function to check login credentials
def login(username, password):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user:
        stored_password_hash = decrypt_hash(user[1])
        stored_password_salt = user[2]
        
        if bcrypt.hashpw(password.encode(),stored_password_salt.encode()) == stored_password_hash.encode() :        
            print("Login successful.")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Main function
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()

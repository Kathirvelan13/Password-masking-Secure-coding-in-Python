from encrypt_and_decrypt import encrypt_password
from cryptography.fernet import Fernet

#generate key and save in file
def generate_key():
    key = Fernet.generate_key()
    with open("secret_key.txt","wb") as f:
        f.write(key)
    print("Key generated successfully")


if __name__ == "__main__":  #this line for no one can import and run the method inside it ,so only we used it

    #uncomment this only for first time...then uncomment it if MySQL password changes
    generate_key()

    encrypted = encrypt_password(input("Enter your Password : "))
    print("Encrypted Password Successfully")
    print("Copy the Encrypted Password and give it as input to encrypt_and_decrypt file ")
    print(encrypted)






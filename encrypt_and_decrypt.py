from cryptography.fernet import Fernet

class Fakestr(str):
    def __str__(self):
        return "*******"
    def __repr__(self):    #for log
        return "*******"

def get_secret_key():
    return open("secret_key.txt","rb").read()

def encrypt_password(password):
    key = get_secret_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = get_secret_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted)


def user_dummy_password():
    encrypted_password = b'gAAAAABpCBWEHi-YB_6a_MEZ0bV9aenOicNPdr0qYuakiZGaSFmVVss4nc9-pSpdzd4UB7p7Cpkn_Y4GRNeFZJkGkL68RoPFVA=='

    return decrypt_password(encrypted_password)





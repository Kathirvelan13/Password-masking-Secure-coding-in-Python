import pymysql
from encrypt_and_decrypt import user_dummy_password

def masked_password():

    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = user_dummy_password(),
        database = "password_masking"

    )

    print("Connection established")
    connection.close()

if __name__ == "__main__":
    masked_password()
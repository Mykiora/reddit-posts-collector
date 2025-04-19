from dotenv import load_dotenv
import os

path = ".env"

if os.path.exists(path):
    load_dotenv()

    user = {"client_id": os.environ["CLIENT_ID"],
            "secret_key": os.environ["SECRET_KEY"],
            "username": os.environ["REDDIT_USERNAME"],
            "password": os.environ["REDDIT_PASSWORD"]}
    
    print(f"Your username is {os.environ['REDDIT_USERNAME']} and your key is {os.environ['SECRET_KEY']}")
else:
    client_id = input("Enter your client ID (personal use script): ")
    secret_key = input("Enter your secret key: ")
    username = input("Enter your Reddit username: ")
    password = input("Enter your Reddit Password: ")

    with open(path, "w") as dotenv_file:
        dotenv_file.write(f"CLIENT_ID={client_id}\nSECRET_KEY={secret_key}\nREDDIT_USERNAME={username}\nREDDIT_PASSWORD={password}")

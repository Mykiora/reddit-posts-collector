from dotenv import load_dotenv
from RedditClient import RedditClient
import os


path = ".env"

if os.path.exists(path):
    load_dotenv()

    user = {"client_id": os.environ["CLIENT_ID"],
            "secret_key": os.environ["SECRET_KEY"],
            "username": os.environ["REDDIT_USERNAME"],
            "password": os.environ["REDDIT_PASSWORD"]}
    
    client = RedditClient(client_id=user["client_id"], secret_key=user["secret_key"], username=user["username"], password=user["password"])
    posts = client.fetch_posts("https://oauth.reddit.com/best?limit=50", client.headers)

    for x in range(50):
        post_data = client.parse_post_data(posts[x])
        client.save_post_content(post_data, x+1)
else:
    client_id = input("Enter your client ID (personal use script): ")
    secret_key = input("Enter your secret key: ")
    username = input("Enter your Reddit username: ")
    password = input("Enter your Reddit Password: ")

    with open(path, "w") as dotenv_file:
        dotenv_file.write(f"CLIENT_ID={client_id}\nSECRET_KEY={secret_key}\nREDDIT_USERNAME={username}\nREDDIT_PASSWORD={password}")

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os


def authenticate(username, password, client_id, secret_key):
    """Sends a request to reddit to get the access token needed to authenticate. Token valid for 24 hours.
       Returns a dictionary containing the token and the headers.

    Args:
        username (str): Reddit account username
        password (str): Reddit account password
        client_id (str): App ID ("personal use script" at https://reddit.com/prefs/apps)
        secret_key (str): Secret key located at https://reddit.com/prefs/apps
    """

    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }

    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

    headers = {"User-Agent": f"windows:{client_id}:v0.0.1 (by /u/{username})"}

    request = requests.post("https://www.reddit.com/api/v1/access_token",
                            auth=auth, data=data, headers=headers)
    
    return {"User-Agent": headers["User-Agent"],
            "Authorization": f"bearer {request.json()['access_token']}"}


def get_post(url, headers):
    """Fetches pieces of information about a post.

    Args:
        url (str): The URL of the post to fetch.
        headers (dict): Headers containing the user agent and the authorization token. (Look authenticate function) 

    Returns:
        dict: A dictionary containing the title, the author's post, the subreddit, the number of ups, the upvote ratio and if gilded or not.
    """
    post = requests.get(url, headers=headers).json()

    title = post[0]["data"]["children"][0]["data"]["title"]
    subreddit = post[0]["data"]["children"][0]["data"]["subreddit"]
    post_text = post[0]["data"]["children"][0]["data"]["selftext"]
    gilded = post[0]["data"]["children"][0]["data"]["gilded"]
    ups = post[0]["data"]["children"][0]["data"]["ups"]
    upvote_ratio = post[0]["data"]["children"][0]["data"]["upvote_ratio"]

    return {"title": title, "subreddit": subreddit, "text": post_text, "gilded": gilded, "ups": ups, "upvote_ratio": upvote_ratio}


path = ".env"

if os.path.exists(path):
    load_dotenv()

    user = {"client_id": os.environ["CLIENT_ID"],
            "secret_key": os.environ["SECRET_KEY"],
            "username": os.environ["REDDIT_USERNAME"],
            "password": os.environ["REDDIT_PASSWORD"]}
    
    headers = authenticate(username=user["username"], password=user["password"], client_id=user["client_id"], secret_key=user["secret_key"])
    print(get_post(url="https://oauth.reddit.com/r/redditdev/comments/3qbll8/429_too_many_requests.json", headers=headers))
else:
    client_id = input("Enter your client ID (personal use script): ")
    secret_key = input("Enter your secret key: ")
    username = input("Enter your Reddit username: ")
    password = input("Enter your Reddit Password: ")

    with open(path, "w") as dotenv_file:
        dotenv_file.write(f"CLIENT_ID={client_id}\nSECRET_KEY={secret_key}\nREDDIT_USERNAME={username}\nREDDIT_PASSWORD={password}")

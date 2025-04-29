from requests.auth import HTTPBasicAuth
import requests


class RedditClient:
    def __init__(self, client_id, secret_key, username, password):
        self.headers = self.authenticate(client_id, secret_key, username, password)
    
    def authenticate(self, client_id, secret_key, username, password):
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

    
    def fetch_posts(self, url, headers):
        try:
            posts = requests.get(url, headers=headers).json()["data"]["children"]
            return posts
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
    

    def parse_post_data(self, post):
        title = post["data"]["title"]
        subreddit = post["data"]["subreddit"]
        post_text = post["data"]["selftext"] if post["data"]["selftext"] != "" else "No text provided by the author"
        gilded = post["data"]["gilded"]
        ups = post["data"]["ups"]
        upvote_ratio = post["data"]["upvote_ratio"]
        post_url = post["data"]["permalink"]

        return {"title": title, "subreddit": subreddit, "post_text": post_text,
                "gilded": gilded, "ups": ups, "upvote_ratio": upvote_ratio, "post_url": post_url}


    def save_post_content(self, post_data, post_id):
        with open("post_data.txt", "a", encoding="utf-8") as f:
            f.write(
                f'POST N°{post_id}\n'
                f'title: {post_data["title"]}\n'
                f'subreddit: {post_data["subreddit"]}\n'
                f'post_text: {post_data["post_text"]}\n'
                f'gilded: {post_data["gilded"]}\n'
                f'ups: {post_data["ups"]}\n'
                f'upvote_ratio: {post_data["upvote_ratio"]}\n'
                f'url: {post_data["post_url"]}\n\n'
            )
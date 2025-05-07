from requests.auth import HTTPBasicAuth
import requests
import os


class RedditClient:
    def __init__(self, client_id: str, secret_key: str, username: str, password: str) -> None:
        """Creates a RedditClient object that will be used to fetch the posts with the API.
           Automatically authenticates and get the headers (User-Agent + Authorization).

        Args:
            client_id (str): App ID ("personal use script" at https://reddit.com/prefs/apps)
            secret_key (str): App Secret key located at https://reddit.com/prefs/apps
            username (str): Reddit account username
            password (str): Reddit account password
        """
        self.headers = self.authenticate(client_id, secret_key, username, password)

    def authenticate(self, client_id: str, secret_key: str, username: str, password: str) -> dict:
        """Sends a request to reddit to get the access token needed to authenticate. Token valid for 24 hours.
        Returns a dictionary containing the token and the headers.

        Args:
            client_id (str): App ID ("personal use script" at https://reddit.com/prefs/apps)
            secret_key (str): App Secret key located at https://reddit.com/prefs/apps
            username (str): Reddit account username
            password (str): Reddit account password
        
        Returns:
            dict: A dictionary containing the User-Agent and the Authorization bearer to use the API.
        """

        data = {"grant_type": "password", "username": username, "password": password}

        auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

        headers = {"User-Agent": f"windows:{client_id}:v0.0.1 (by /u/{username})"}

        request = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data=data,
            headers=headers,
        )

        return {
            "User-Agent": headers["User-Agent"],
            "Authorization": f"bearer {request.json()['access_token']}",
        }

    def fetch_posts(self, headers: dict[str], subreddit: str = "", filter: str = "hot", limit: int = 50) -> list[dict] | None:
        """Sends a request to get a list of posts.

        Args:
            headers (dict): Dict containing the User-Agent and the Authorization bearer.
            subreddit (str, optional): Subreddit to fetch. Only the name and including "/r". Defaults to "".
            filter (str, optional): Homepage or subreddit filter. (best, hot, top, controversial, rising, new) Defaults to "hot".
            limit (int, optional): Number of posts fetched. Defaults to 50.

        Returns:
            list[dict] | None: A list of dictionaries containing posts and information about them. None if the requests fails. 
        """
        try:
            posts = requests.get(
                f"https://oauth.reddit.com/{subreddit}/{filter}?limit={limit}",
                headers=headers,
            ).json()["data"]["children"]
            return posts
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def parse_post_data(self, post: list[dict]) -> dict:
        """Takes ONE particular post dictionary gotten from the fetch_posts function and parses its data.

        Args:
            post (list[dict]): A list of dictionaries containing information about a post. Such as the title,
                               the number of upvotes, the messages, etc...

        Returns:
            dict: A dictionary containing all the needed information. 
        """
        title = post["data"]["title"]
        subreddit = post["data"]["subreddit"]
        post_text = (
            post["data"]["selftext"]
            if post["data"]["selftext"] != ""
            else "No text provided by the author"
        )
        gilded = post["data"]["gilded"]
        ups = post["data"]["ups"]
        upvote_ratio = post["data"]["upvote_ratio"]
        post_url = post["data"]["permalink"]

        return {
            "title": title,
            "subreddit": subreddit,
            "post_text": post_text,
            "gilded": gilded,
            "ups": ups,
            "upvote_ratio": upvote_ratio,
            "post_url": post_url,
        }

    def save_post_content(self, post_data: dict, post_id: int) -> None:
        """Saves the post data in a text file.

        Args:
            post_data (dict): The dicionary gotten from the parse_post_data function.
            post_id (int): An arbitrary number (not tied to anything) acting as a visual help in the text file.
        """
        if not os.path.exists("data"):
            os.mkdir("data")

        with open("data/post_data.txt", "a", encoding="utf-8") as f:
            f.write(
                f"POST N°{post_id}\n"
                f'title: {post_data["title"]}\n'
                f'subreddit: {post_data["subreddit"]}\n'
                f'post_text: {post_data["post_text"]}\n'
                f'gilded: {post_data["gilded"]}\n'
                f'ups: {post_data["ups"]}\n'
                f'upvote_ratio: {post_data["upvote_ratio"]}\n'
                f'url: {post_data["post_url"]}\n\n'
            )

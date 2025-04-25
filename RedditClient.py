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


    def get_post(self, url, headers):
        """Fetches pieces of information about a post.

        Args:
            url (str): The URL of the post to fetch.
            headers (dict): Headers containing the user agent and the authorization token. (Look authenticate function) 

        Returns:
            str: A giant string containing all the info about the posts (you could feed it to a LLM)
        """
        posts = requests.get(url, headers=headers).json()["data"]["children"]
        info = ""

        for x in range(50):
            title = posts[x]["data"]["title"]
            subreddit = posts[x]["data"]["subreddit"]
            post_text = posts[x]["data"]["selftext"] if posts[x]["data"]["selftext"] != "" else "No text provided by the author"
            gilded = posts[x]["data"]["gilded"]
            ups = posts[x]["data"]["ups"]
            upvote_ratio = posts[x]["data"]["upvote_ratio"]
            post_url = posts[x]["data"]["permalink"]

            info += f"POST N°{x+1}\ntitle: {title}\nsubreddit: {subreddit}\npost_text: {post_text}\ngilded: {gilded}\nups: {ups}\nupvote_ratio: {upvote_ratio}\nurl: {post_url}\n\n"

        return info
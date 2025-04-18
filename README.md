# reddit-latest-posts

## Description
This program collects posts and their information from the main reddit page depending on a sorting filter, then uses a local LLM to summarize the content, all that without the need to open the browser.

## Requirements
Before being able to use the script, you need your own secret key that you will be the only one to use. In order to get that key, you have to create a reddit app. Fortunately, it's quick and easy.

Here is how to do it:
1) Follow this [LINK](https://www.reddit.com/prefs/apps).
2) Click on "are you a developer? create an app.." button in the top left.
3) Give it a name, maybe a description. When prompted with "web app", "installed app" or "script", choose script. use "http://localhost:8080" for the redirect uri. It just means the app is running on your own computer.
4) Click the "create app" button and copy "secret", which is your key.

## Filters
**Hot** - ranks using votes and post age.
**New** - displays the most recently published posts.
**Rising** - populates posts with lots of recent votes and comments.
**Top** - shows you the highest vote count posts from a specified time range

Reference: https://www.reddit.com/r/blog/comments/o5tjcn/evolving_the_best_sort_for_reddits_home_feed/?utm_source=share&utm_medium=ios_app&utm_name=ioscss&utm_content=1&utm_term=1
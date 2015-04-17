import praw
import time

r = praw.Reddit(user_agent= 'alg.cubing.net linker thing')
r.login()

def run_bot():
    subreddit = r.get_subreddit('')
    comments = subreddit.get_comments
    for comment in comments:
        comment_text = comment.body
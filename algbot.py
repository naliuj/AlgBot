import praw
import time
import algbot_oauth
import alg_linker

r = algbot_oauth.login()
subreddit = r.get_subreddit('naliuj')

def run_bot():
    alg_linker.run(subreddit)

while True:
    try:
        run_bot()
        time.sleep(10)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print('error {0}'.format(e))
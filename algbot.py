import praw
import time
import re
import algbot_oauth

regex = re.compile(r"`(3x3): *(([RLFBUDrlfbudxyz]|[RLFBUD]w|[ 2'])+)`?")
r = algbot_oauth.login()

def run_bot():
    subreddit = r.get_subreddit('naliuj')
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        with open('comment_ids.txt','r') as file:
            cachedComments = file.readlines()
        if comment.id+'\n' in cachedComments:
            writeReply(comment.body, comment)

# parses a body of text and returns algs
def getAlgs(text):
    if re.match(regex, text):
        m = re.match(regex, text)
        alg = m.group(2)
        yield alg 						# yields that alg and continues to search for more algs

def writeReply(commentBody,comment):
    algs = [alg for alg in getAlgs(commentBody)]
    if len(algs) > 0:
        replyBody = '';
        for alg in algs:
            replyBody += ('''alg.cubing.net link:
[`%s`](https://alg.cubing.net/?alg=%s)

^^I ^^am ^^a ^^bot. ^^Please ^^Message ^^the ^^moderators ^^of ^^/r/Cubers ^^if ^^there ^^are ^^any ^^issues.''') % (alg, alg)
        comment.reply(replyBody)
        with open('comment_ids.txt','w') as file:
            file.write(comment.id+'\n')
        print('replied to: '+comment.id)

# we want to keep scanning
while True:
    try:
        run_bot()
        time.sleep(10)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print('error {0}'.format(e))
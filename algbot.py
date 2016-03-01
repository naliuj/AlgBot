import praw
import time
import re
import algbotOAuth

commentCache = [] # add id's to replied comments here
blacklist = ['algbot','rubiksbot']

regex = re.compile(r"`3x3: *(([RLFBUDrlfbudxyz]|[RLFBUD]w|[ 2'])+)`?")

def run_bot():
    subreddit = r.get_subreddit('naliuj')
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        if comment.author.name.lower() not in blacklist and comment.id not in commentCache:
            writeReply(comment.body, comment)
            commentCache.append(comment.id)

# parses a body of text and returns algs
def getAlgs(text):
        if re.match(text, regex):
            m = re.match(text, regex)
            alg = m.group(1)
            yield alg 						# yields that alg and continues to search for more algs

def writeReply(commentBody,comment):
    algs = [alg for alg in getAlgs(commentBody)]
    if len(algs) > 0:
        replyBody = '';
        for alg in algs:
            replyBody += ('''Alg: `%s`

[alg.cubing.net Link](https://alg.cubing.net/?alg=%s)\n\n''') % (alg, alg)

        replyBody += '^^(I am a bot. Please Message the moderators of /r/Cubers if there are any issues.)'
        comment.reply(replyBody)

r = algbotOAuth.login()
# we want to keep scanning
while True:
    try:
        run_bot()
        time.sleep(10)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print('error {0}'.format(e))

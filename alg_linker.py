import praw
import re

regex = re.compile(r"`(2x2|3x3|4x4): *(([RLFBUDMSErlfbudxyz]|[RLFBUD]w|[ 2'])+)`?")

def run(subreddit):
    comments = subreddit.get_comments(limit=25)
    with open('comment_ids.txt','r') as f:
        seen_comments = f.read().splitlines()
    for comment in comments:
        if comment.id not in seen_comments:
            writeReply(comment.body, comment)

def getAlgs(text):
    if re.match(regex, text):
        m = re.match(regex, text)
        alg = m.group(2)
        yield alg

def getSize(text):
    m = re.match(regex, text)
    return {
        '2x2':'&puzzle=2x2x2',
        '3x3':'&puzzle=3x3x3',
        '4x4':'&puzzle=4x4x4'
        }[m.group(1)]

def writeReply(commentBody,comment):
    algs = [alg for alg in getAlgs(commentBody)]
    if len(algs) > 0:
        replyBody = '';
        size = getSize(commentBody)
        for alg in algs:
            replyBody += ('''alg.cubing.net link:
[`%s`](https://alg.cubing.net/?alg=%s%s)

^^I ^^am ^^a ^^bot. ^^Please ^^Message ^^the ^^moderators ^^of ^^/r/Cubers ^^if ^^there ^^are ^^any ^^issues.''') % (alg, alg, size)
        comment.reply(replyBody)
        with open('comment_ids.txt','a') as f:
            f.write(comment.id)
            f.write('\n')
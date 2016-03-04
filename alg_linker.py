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
        m = re.findall(regex, text)
        for match in m:
            alg = match
            print(alg)
            yield alg

def getSize(alg):
        return {
            '2x2':'&puzzle=2x2x2',
            '3x3':'&puzzle=3x3x3',
            '4x4':'&puzzle=4x4x4'
            }[alg[0]]

def writeReply(commentBody,comment):
    algs = [alg for alg in getAlgs(commentBody)]
    if len(algs) > 0:
        replyBody = 'alg.cubing.net:\n\n'
        for alg in algs:
            replyBody += '[`%s`](https://alg.cubing.net/?alg=%s%s)\n\n' % (alg[1], alg[1], getSize(alg))
        replyBody += '^^I ^^am ^^a ^^bot. ^^Please ^^Message ^^the ^^moderators ^^of ^^/r/Cubers ^^if ^^there ^^are ^^any ^^issues.'
        comment.reply(replyBody)
        with open('comment_ids.txt','a') as f:
            f.write(comment.id)
            f.write('\n')
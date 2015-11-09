import praw
import time
import re

r = praw.Reddit(user_agent= 'alg.cubing.net linker for /r/cubers')
r.login('AlgBot', )

commentCache = [] # add id's to replied comments here
blacklist = ['algbot','rubiksbot']

regex = re.compile(r"[RLFBUDrlfbudxyz][2']?");

def run_bot():
    subreddit = r.get_subreddit('naliuj')
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        if comment.author.name.lower() not in blacklist:
            commentBody=comment.body
            writeReply(commentBody,comment)
            commentCache.append(comment.id)

# parses a body of text and returns algs
def getAlgs(text):
    while text.find('[') != -1 and text.find(']') != -1: 	# determines that there exists and alg
        alg = text[text.find('[')+1:text.find(']')] 		# gets that alg
        text = text.replace('[' + alg + ']', '') 		# removes that piece of text to find next alg
        if regex.match(alg):
            print(alg)
            yield alg 						# yields that alg and continues to search for more algs

def writeReply(commentBody,comment):
    for alg in getAlgs(commentBody):
        print(alg)
        replyBody =('''Alg: `%s`

[alg.cubing.net Link](https://alg.cubing.net/?alg=%s)

^^I ^^am ^^a ^^bot. ^^Please ^^Message ^^the ^^moderators ^^of ^^/r/Cubers ^^if ^^there ^^are ^^any ^^issues.''') % (alg, alg)
        comment.reply(replyBody)

# we want to keep scanning
while True:
    run_bot()
    time.sleep(10)

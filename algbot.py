import praw
import time

r = praw.Reddit(user_agent= 'alg.cubing.net linker thing')
r.login()

def run_bot():
    subreddit = r.get_subreddit('')
    comments = subreddit.get_comments
    for comment in comments:
        # should I reply to this comment
        # if yes, reply = writeReply(comment.body)
        # then continue
       
# parses a body of text and returns algs
def getAlgs(text):
	while text.find('[') != -1 and text.find(']') != -1: 	# determines that there exists and alg
		alg = text[text.find('[')+1:text.find(']')] 		# gets that alg
		text = text.replace('[' + alg + ']', '') 			# removes that piece of text to find next alg
		yield alg 											# yields that alg and continues to search for more algs

def writeReply(commentBody):
	replyBody = 'I converted your algs into alg.cubing.net algs. Here there are: '
	for alg in getAlgs(commentBody):
		# append to replyBody your link 

	# add signature

# we want to keep scanning
while True: 
	run_bot();
import praw
import random
import time
import datetime

# this is the login information for our bot
username='emolyandmatolda'
password='Emmy646'
client_id='0xYrv9mLQixeBg'
client_secret='gupVZAcCZHyB2woYEiI07O6cKao'
user_agent='Comp40EB'

# connect to reddit 
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password,
    )

# FIXME (task 1): the submission variable should be a praw submission object that
# points to the bot political discussion thread at
# https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/
# HINT: there is a one-line command in the praw quick-start guide
# that accomplishes this task.
submissions=[]
for submission in reddit.subreddit('csci040').hot(limit=10):
    submissions.append(submission)
print('sub', submissions)
    
#submission= reddit.submission(url='https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/')

for sub in submissions:
    all_comments= submission.comments.list()

    print(all_comments)

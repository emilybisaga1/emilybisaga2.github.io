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
submission=None

# in an infinite loop, we will look for comment in the post that we can reply to
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())

    # FIXME (task 2): get a list of all of the comments in the submission
    all_comments=[]
    # HINT1: there is a one-line command in the praw quick-start guide
    # that accomplishes this task.
    # HINT2: whenever we work on a program, you need to somehow check that the
    # things your programming is doing are correct.  In this case, one thing
    # we can do is to check the length of the all_comments variable.
    # You should manually ensure that the printed length is the same as the
    # length displayed on reddit.  If it's not, then there are some comments
    # that you are not correctly identifying, and you need to figure out
    # which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 3): filter all_comments to remove comments that were generated by your bot
    not_my_comments=[]
    # HINT1: completing this task requires only a single for loop and a single if statement.
    # The PRAW quick-start guide has the contents of the for loop/if statement.
    # HINT2: as before, you need to check that your code is working somehow.
    # reddit does not provide any list of comments generated by your bot,
    # but you can easily check this number manually by subtracting the number
    # of comments you know you've posted from the number above.
    print('len(not_my_comments)=',len(not_my_comments))

    # FIXME (task 4): filter the list to also remove comments that you've already replied to
    comments_without_replies=[]
    # HINT1: completing this task requires only a single for loop and a single if statement.
    # The PRAW quick-start guide has the contents of the for loop/if statement.
    # HINT2: again, you need to check that this is working
    print('len(comments_without_replies)=',len(comments_without_replies))

    # FIXME (task 5): randomly select one of the comments that we haven't replied to yet
    # HINT: There is a function in python's random module for doing this.
    # See the documentation at https://docs.python.org/3/library/random.html
    comment = None

    # FIXME (task 6): generate some random text for your comment;
    # your message must clearly identify itself as a bot
    # HINT: This is the same as lab 13.
    text=''

    # FIXME (task 7): post a reply to the selected comment
    # HINT: We covered how to do this in class on 12 Nov.
    # See the reddit.py lecture notes or the PRAW quick start guide.

    # FIXME (task 8): check all submissions in the /r/csci040 subreddit to see if your
    # bot has not created a top-level comment in that submission.  If it has not,
    # then create a top-level comment.
    # HINT1: The PRAW quick-start guide contains all the information you need to know
    # about PRAW to complete this task.
    # HINT2: The code for this task will have to be placed in multiple places throughout
    # this file.

    # sleep for 10-15 minutes so that you don't overload reddit
    time.sleep(10*60+random.randrange(5*60))

import praw
from threading import Timer
from os import environ

# reddit api login
reddit = praw.Reddit(client_id=environ['CLIENT_ID'],
                     client_secret=environ['CLIENT_SECRET'],
                     username=environ['USERNAME'],
                     password=environ['REDDITPWD'],
                     user_agent=environ['USER_AGENT'])


def bidkaro():
    flag = 1
    for submission in reddit.subreddit('signupsforpay').new(limit=1):
        # for submission in reddit.subreddit('testingground4bots').new(limit=1):
        title = submission.title
        if 'onlyfans' in title.lower() or 'only fans' in title.lower():
            file = open('submissionID.txt', 'r')
            for line in file:
                if submission.id in line:
                    flag = 0
                    file.close()
                    break
        # if 'onlyfans' in title.lower() and submission not in bidDone:
        if 'onlyfans' in title.lower() and flag == 1 or 'only fans' in title.lower() and flag == 1:
            submission.reply('$bid')
            file = open('submissionID.txt', 'a')
            file.write(submission.id)
            file.close()
            print('Commented on', title)
            print('Waiting for the next post.....')
    Timer(2, bidkaro).start()
    #bidkaro()


bidkaro()

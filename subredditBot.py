import praw

botProfile= '' #I am assuming you have a moderator bot with proper dev script creds in a local praw.ini
newSubreddit = '' #Add it in
reddit = praw.Reddit(botProfile)

with open('banned_souls.txt', 'r') as souls:
    for user in souls:
        reddit.subreddit(newSubreddit).contributor.add(user.rstrip())
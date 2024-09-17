import praw
import pandas as pd
from textblob import TextBlob
from dotenv import load_dotenv
import os

# Load environment variables (Reddit API credentials)
load_dotenv()

# Reddit API credentials
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))


# Function to perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'


# Collect Reddit posts from a subreddit
def get_reddit_posts(subreddit_name, post_limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for submission in subreddit.hot(limit=post_limit):
        posts.append([submission.title, get_sentiment(submission.title)])

    return posts


# usage
subreddit_name = "cscareerquestions"  # Change this to any subreddit
posts = get_reddit_posts(subreddit_name, post_limit=100)

# Create a DataFrame and save to CSV
df = pd.DataFrame(posts, columns=['Post', 'Sentiment'])
df.to_csv(f'reddit_{subreddit_name}_sentiment_analysis.csv', index=False)

print(f"Sentiment analysis completed and saved to 'reddit_{subreddit_name}_sentiment_analysis.csv'")

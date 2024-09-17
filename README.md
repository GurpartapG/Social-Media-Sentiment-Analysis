# Reddit Sentiment Analysis for r/cscareerquestions
This project performs sentiment analysis on Reddit posts from the r/cscareerquestions subreddit, allowing users to analyze the general sentiment (positive, negative, or neutral) of posts regarding career advice in the tech industry. The script scrapes the top posts from the subreddit using Reddit's API and analyzes the sentiment of the post titles using TextBlob.

## Project Motivation
The motivation behind this project is to monitor and analyze sentiment trends in discussions around career development, job seeking, and advice in the computer science and software engineering field. By understanding the sentiment in career-related posts, it provides useful insights for career strategizing, determining common frustrations, and identifying opportunities for improvement.

## Flexibility
While this project is currently set up to analyze posts from the r/cscareerquestions subreddit, you can easily modify the script to analyze sentiment from any subreddit of your choice. To do so, simply replace the subreddit_name in the script with the desired subreddit:
subreddit_name = "desired_subreddit"

## Features
- Fetches posts from the r/cscareerquestions subreddit.
- Analyzes post titles for sentiment (positive, neutral, or negative).
- Outputs results in CSV format.
- Utilizes PRAW (Python Reddit API Wrapper) to fetch Reddit posts.
- Uses TextBlob for sentiment analysis.

## Installation
1. Clone the repository to your local machine
2. Navigate to the project directory
3. Install the required dependencies (Python 3.x, PRAW, TextBlob, Pandas, dotenv):
   pip install praw textblob pandas python-dotenv
4. Add your Reddit API credentials in the .env file (example template below):
   CLIENT_ID=your-client-id  
CLIENT_SECRET=your-client-secret  
USER_AGENT=your-user-agent
6. Run the script


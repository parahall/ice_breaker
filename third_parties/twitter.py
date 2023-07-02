import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger("twitter")

data = [
    {
        "edit_history_tweet_ids": ["1659558201040203777"],
        "id": "1659558201040203777",
        "text": "Working on my slides for @droidconBerlin This times I'm going to share our journey of building BFF aka Backend for Frontend. I'm curious, out of all my followers, who familiar with this concept and who actually worked with that?",
    },
    {
        "edit_history_tweet_ids": ["1659558198649470977"],
        "id": "1659558198649470977",
        "text": "I really like this as it outlines what are the capabilities of GPT4 and ask the question - Is it intelligent? The revolution is here, you like it or not, so it's matter of decision if you want to embrace it or being left behind.https://youtu.be/qbIk7-JPB2c",
    },
    {
        "edit_history_tweet_ids": ["1659558196577443840"],
        "id": "1659558196577443840",
        "text": "Excellent morning read: https://discord.com/blog/how-discord-stores-trillions-of-messages Very interesting Discord journey about their scale, challenges, approach on choosing the right DB and migration process. Must for an every engineer :)",
    },
    {
        "edit_history_tweet_ids": ["1659558193217896452"],
        "id": "1659558193217896452",
        "text": 'Quick reminder to my fellow developers that writing "beautiful code with a lot of abstraction" might actually hurt your teams performance rather than speed up future features.',
    },
    {
        "edit_history_tweet_ids": ["1659558190843846657"],
        "id": "1659558190843846657",
        "text": "Wowowow! My story about what we did at Ukraine/Poland border was chosen to be featured on HackerNoon "
        "for over 134,000 subscribers!🥹 🎉 Besides, wanna be part of this story too? Read and share it!: "
        "https://hackernoon.com/unleashing-the-power-of-technology-and-kindness-the-moving-tale-of"
        "-volunteering #technology #startup #betterhuman #volunteer",
    },
]


def scrape_user_tweets(username, num_tweets=5):
    """Scrapes a Twitter users's original tweets (i.e., not retweets or
    replies) and returns them as a list of dictionaries.Each dictionary has
    three fields: "time_posted" (relative to now), "text", and "url".
    """
    print(f"Got username: {username}")
    tweet_list = []
    for tweet in data:
        if "RT @" not in tweet["text"] and not tweet["text"].startswith("@"):
            tweet_dict = {
                "text": tweet["text"],
                "url": f"https://twitter.com/{username}/status/{tweet['id']}",
            }
            tweet_list.append(tweet_dict)
    return tweet_list

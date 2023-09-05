from typing import List
from abc import ABC, abstractmethod
import time


class SocialChannel(ABC):
    def __init__(self, followers: int):
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str) -> None:
        pass


class YouTubeChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Posting on YouTube: {message} to {self.followers} followers")


class FacebookChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Posting on Facebook: {message} to {self.followers} followers")


class TwitterChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Posting on Twitter: {message} to {self.followers} followers")


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    current_time = int(time.time())
    for post in posts:
        if post.timestamp <= current_time:
            for channel in channels:
                channel.post_message(post.message)


youtube_channel = YouTubeChannel(followers=1000000)
facebook_channel = FacebookChannel(followers=500000)
twitter_channel = TwitterChannel(followers=200000)

channels = [youtube_channel, facebook_channel, twitter_channel]

posts = [
    Post("YouTube post", 1632345600),
    Post("Facebook post", int(time.time())),
    Post("Twitter post", int(time.time())),
]

process_schedule(posts, channels)

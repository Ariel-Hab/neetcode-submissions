from typing import List

class Tweet:
    def __init__(self, tweetId: int, userId: int):
        self.tweetId = tweetId
        self.userId = userId

class User:
    def __init__(self):
        self.following = set()

    def follow(self, followeeId: int) -> None:
        self.following.add(followeeId)

    def unfollow(self, followeeId: int) -> None:
        self.following.discard(followeeId)

class Twitter:
    def __init__(self):
        self.tweets: List[Tweet] = []
        self.users: dict[int, User] = {}

    def getUser(self, userId: int) -> User:
        if userId not in self.users:
            self.users[userId] = User()
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(Tweet(tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        user = self.getUser(userId)
        for tweet in reversed(self.tweets):
            if tweet.userId == userId or tweet.userId in user.following:
                result.append(tweet.tweetId)
                if len(result) == 10:
                    break
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        follower = self.getUser(followerId)
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.getUser(followerId)
        follower.unfollow(followeeId)
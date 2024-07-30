class Twitter:

    def __init__(self):
        from queue import PriorityQueue
        self.followers_id = {}
        self.tweets_map = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweets_map:
            self.tweets_map[userId] = []
        
        if not userId in self.followers_id:
            self.followers_id[userId] = set()
            self.followers_id[userId].add(userId)
        self.tweets_map[userId].append((-self.count,tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        from queue import PriorityQueue
        max_heap = PriorityQueue()
        followers = self.followers_id.get(userId, [])
        for users_ in followers:
            tweets = self.tweets_map.get(users_, [])
            for tweet in tweets:
                max_heap.put(tweet)
        ans = []
        count_ = 0

        while max_heap.qsize() and count_ < 10:
            _, tweet_ = max_heap.get()
            ans.append(tweet_)
            count_ += 1

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followers_id:
            self.followers_id[followerId] = set()
            self.followers_id[followerId].add(followerId)
        self.followers_id[followerId].add(followeeId) 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.followers_id:
            return
        self.followers_id[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
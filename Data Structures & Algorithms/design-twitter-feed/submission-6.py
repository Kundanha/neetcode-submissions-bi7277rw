class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweet = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count, tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for f in self.followMap[userId]:
            if f in self.tweet:
                index = len(self.tweet[f]) - 1
                count, recentTweet = self.tweet[f][index]
                minHeap.append([count, recentTweet, f, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweet, followeeId, i = heapq.heappop(minHeap)
            res.append(tweet)
            if i >= 0:
                count, tweet = self.tweet[followeeId][i]
                heapq.heappush(minHeap, [count, tweet, followeeId, i-1])
        return res
                

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
        

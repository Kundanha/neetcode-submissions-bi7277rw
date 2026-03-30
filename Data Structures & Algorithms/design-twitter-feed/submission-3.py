from collections import defaultdict
import heapq
from typing import List

class Twitter:
    """
    Design Twitter (LeetCode 355) — Heap + k-way merge approach.

    Core idea:
    - Har user ke tweets ko time-order me store karo.
    - NewsFeed nikalte time: user + followees ke "latest tweet pointers" ko heap me daalo,
      then heap se repeatedly most-recent tweet pop karo (max 10), aur usi followee ka next older tweet push karo.
    """

    def __init__(self):
        # Global timestamp counter (we keep it decreasing: 0, -1, -2, ...)
        # Why decreasing? Because Python heap is min-heap, and "most recent" ko "smallest number" bana dete hain.
        self.time = 0

        # tweetMap[userId] = list of [time, tweetId]
        # Tweets are appended in chronological order; last element = most recent tweet.
        self.tweetMap = defaultdict(list)

        # followMap[followerId] = set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a tweet:
        - Store [time, tweetId] in tweetMap.
        - Decrement time so newer tweets have smaller time => pop earlier from min-heap.
        """
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Return up to 10 most recent tweetIds in user's news feed.

        Algorithm (k-way merge using heap):
        1) Ensure user follows themselves (so own tweets included).
        2) For each followee, push their most recent tweet into heap:
           heap entry = [time, tweetId, followeeId, nextIndex]
           where nextIndex points to that followee's next older tweet.
        3) Repeat up to 10 times:
           - Pop the most recent tweet (smallest time).
           - Append tweetId to result.
           - If that followee has older tweets (nextIndex >= 0), push next older tweet into heap.
        """
        res = []
        minHeap = []

        # Include user's own tweets in feed
        self.followMap[userId].add(userId)

        # Seed heap with the latest tweet of each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1  # most recent tweet index
                time, tId = self.tweetMap[followeeId][index]
                # nextIndex = index - 1 => next older tweet pointer for this followee
                minHeap.append([time, tId, followeeId, index - 1])

        heapq.heapify(minHeap)

        # Extract up to 10 most recent tweets across all followees
        while minHeap and len(res) < 10:
            time, tId, followeeId, index = heapq.heappop(minHeap)
            res.append(tId)

            # Push the next older tweet from the same followee (if exists)
            if index >= 0:
                nextTime, nextTId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [nextTime, nextTId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """followerId starts following followeeId."""
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """followerId unfollows followeeId (ignore if not following)."""
        self.followMap[followerId].discard(followeeId)
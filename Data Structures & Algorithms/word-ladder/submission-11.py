class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        q = deque([beginWord])
        visited = set(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for n in nei[pattern]:
                        if n not in visited:
                            q.append(n)
                            visited.add(n)
            res+=1
        return 0

        
        
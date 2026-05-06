class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        alpha = "abcdefghijklmnopqrstuvwxyz"
        q = deque([beginWord])
        visited = set(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if endWord == word:
                    return res
                for i in range(len(word)):
                    for a in alpha:
                        newWord = word[:i] + a + word[i+1:]
                        if newWord in wordSet and newWord not in visited:
                            q.append(newWord)
                            visited.add(newWord)
            res+=1
        return 0

        
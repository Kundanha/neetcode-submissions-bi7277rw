class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {c: i for i, c in enumerate(order)}

        def compare(word):
            return [orderIndex[c] for c in word]
        
        return words == sorted(words, key=compare)
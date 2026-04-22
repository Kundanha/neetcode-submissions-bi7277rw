class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        cur = ""
        while i < len(word) and j < len(abbr):
            if word[i] != abbr[j]:
                if abbr[j].isalpha() or abbr[j] == "0":
                    return False
                else:
                    num = 0
                    while j < len(abbr) and not abbr[j].isalpha():
                        num = num * 10  + int(abbr[j])
                        j+=1
                    i+=num
            else:
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)

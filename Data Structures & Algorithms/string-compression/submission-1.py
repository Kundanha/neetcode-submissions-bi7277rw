class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        s = chars[0]
        count = 1
        for i in range(1, len(chars)):
            cur = chars[i]
            prev = chars[i-1]
            if cur != prev:
                if count > 1:
                    s+=str(count)
                s+=cur
                count = 1
            else:
                count+=1
        if count > 1:
            s += str(count)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
            

        
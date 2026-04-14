class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        for k in range(len(customers)):
            if grumpy[k] == 0:
                base += customers[k]
        i = -1
        j = -1
        total = 0
        maxtotal = 0
        while True:
            l1 = False
            l2 = False

            while i < len(customers) - 1 and i - j < minutes:
                i+=1
                if grumpy[i] == 1:
                    total += customers[i]
                l1 = True
            
            while j < i and i - j == minutes:
                if i - j == minutes:
                    maxtotal = max(maxtotal, total)
                j+=1
                if grumpy[j] == 1:
                    total -= customers[j]
                l2 = False
                break
            if not l1 and not l2:
                break
        return maxtotal + base

        
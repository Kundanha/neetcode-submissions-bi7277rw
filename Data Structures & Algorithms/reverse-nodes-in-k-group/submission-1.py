# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(cur, k):
            while cur and k>0:
                cur=cur.next
                k-=1
            return cur

        kth = getKth(head, k - 1)        # 🔁 k-1: group ka kth (last) node
        if not kth:                      # ➕ base case: k se kam nodes -> as-is
            return head
        groupNext = kth.next
            
        newHead = self.reverseKGroup(groupNext, k)
            #reverse linkedlist

        prev = newHead
        cur = head
        while cur != groupNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

        
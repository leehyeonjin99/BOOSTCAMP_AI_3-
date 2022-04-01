class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        L = []
        while True:
            L.append(head.val)
            head = head.next
            if not head:
                break
        left = left-1
        right = right-1
        mid = L[left:right+1]
        mid.reverse()
        L = L[:left] + mid + L[right+1:]
        result = ListNode(L[-1])
        L = L[:-1]
        L.reverse()
        for idx, i in enumerate(L):
            temp = ListNode(i)
            temp.next = result
            result = temp
        return result
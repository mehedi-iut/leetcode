l1 = [2,4,3]
l2 = [5,6,4]
## output = [7, 0, 8]

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        val = total % 10
        carry = total // 10

        curr.next = ListNode(val)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


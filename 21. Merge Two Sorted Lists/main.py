def main():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
    
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    result = mergeTwoLists(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
    

if __name__ == "__main__":
    main()
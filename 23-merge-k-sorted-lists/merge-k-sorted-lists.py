# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists == [] or lists == None:
            return None
        else:
            pq = []
            for i in range(len(lists)):
                if lists[i] != None:
                    item = (lists[i].val, i, lists[i])
                    heapq.heappush(pq, item)
            dummy = ListNode(0)
            p = dummy

            while pq != []:
                heap_item = heapq.heappop(pq)
                p.next = heap_item[2]
                p = p.next
                if heap_item[2].next != None:
                    item = (heap_item[2].next.val, heap_item[1], heap_item[2].next)
                    heapq.heappush(pq, item)
            return dummy.next
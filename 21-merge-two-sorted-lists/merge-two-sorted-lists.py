class Solution(object):
    def mergeTwoLists(seld, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = current = list1
        list1 = list1.next

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head 
        
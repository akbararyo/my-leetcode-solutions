# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1)
        # print(l2)
        num1 =  []
        num2 = []
        currentNode1 = l1
        currentNode2 = l2
        # l1
        while currentNode1:
            num1.append(currentNode1.val)
            # print(f"{currentNode1.val}")
            currentNode1 = currentNode1.next
        # print(f"num1 = {num1}")
        # l2
        while currentNode2:
            num2.append(currentNode2.val)
            # print(f"{currentNode2.val}")
            currentNode2 = currentNode2.next
        # print(f"num2 = {num2}")

        #sum
        str1=""
        str2=""
        for i in  range(len(num1)):
            str1 += str(num1[len(num1)-(i+1)]) #-(i+1) for insert it from backwards
        for i in  range(len(num2)):
            str2 += str(num2[len(num2)-(i+1)])
        sum=int(str1)+int(str2)
        # print(sum)

        submit=[]
        str_sum = str(sum)
        len_sum = len(str(sum))
        for i in range(len_sum):
            submit.extend([int(str_sum[len_sum - (i+1)])])
        # print(submit)

        def list_to_linked(arr):
            head = ListNode(arr[0])
            current = head

            for i in range(1,len(arr)):
                current.next = ListNode(arr[i])
                current = current.next
            return head
        
        return list_to_linked(submit)


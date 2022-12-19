# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) ->  ListNode:
        str1 = ""
        str2 = ""

        current = l1
        while(current != None):
            tmp = str(current.val) + str1
            str1 = tmp
            current = current.next

        current = l2
        while(current != None):
            tmp = str(current.val) + str2
            str2 = tmp
            current = current.next

        sumInt = int(str1) + int(str2)
        sumString = str(sumInt)
        head = None
        lastNode = None
        
        
        for i in range(len(sumString)):
            currentNode = ListNode(int(sumString[i]),None)
            if head == None:
                head = currentNode
                lastNode = currentNode
            else: 
                lastNode.next = currentNode 
                lastNode = currentNode 
        
        head =self.reverseList(head)
        
        return head


    def reverseList(self,l1):
        currentNode = l1
        prevNode = None
        
        while(currentNode != None):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        l1 = prevNode

        return l1

    def initList(self,tab):
        head = ListNode(tab[0],None)
        currentNode = head

        for i in range(1,len(tab)):
            currentNode.next = ListNode(tab[i],None)
            currentNode = currentNode.next
        return head

def printList(list):
    currentNode = list
    while(currentNode != None):
        print(currentNode.val)
        currentNode = currentNode.next

soluce = Solution()
list1 = soluce.initList([2,4,3])
list2 = soluce.initList([5,6,4])


list3 = soluce.addTwoNumbers(list1,list2)
printList(list3)


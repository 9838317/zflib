"""
This program genarates a linked List

Makell(List):
     tansfer the list into a linked list, return the head  
"""

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next  = None

    def __str__(self):
        return self.getList()

    def getList(self):
        string  = ''
        pointer = self
        while pointer != None:
            string  = string + str(pointer.value) + '--> '
            pointer = pointer.next 
        string += 'None'         
        return string
        
class Makell(object):
    def __init__(self, paraList):
        self.head = self.makell(paraList)
    
    def makell(self, paraList):
        head    = ListNode(paraList[0])
        pointer = head
        for i in paraList[1:]:
            temp = ListNode(i)
            pointer.next = temp
            pointer = pointer.next
        return head

    def __str__(self):  
        return self.head.getList()    

if __name__ == '__main__':
    import mrd
    commonList     = mrd.Random().ran(10,20)
    linkList       = Makell(commonList)
    print 'original array is', commonList
    print 'try call linklist', linkList.head

        
        

class Node:

    def __init__(self):
        self.prev = None
        self.next = None
        self.key = ""

class DLL:
    
    def __init__(self):
        self.head = None #head of the DLL
        self.tail = None #tail of the DLL

    def append(self, value):
        newNode = Node()
        newNode.key = value

        if self.head is None:
            self.head = newNode
            return

        crawler = self.head

        while(crawler):
            if crawler.next is None:
                crawler.next = newNode
                self.tail = newNode
                return
            crawler = crawler.next


    def prepend(self, value):
        newNode = Node()
        newNode.key = value

        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode

        return

    def print(self):
        crawler = self.head

        while(crawler):
            print(crawler.key)
            crawler = crawler.next
from arraySortLib import quickSort

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

def defaultComparator(node, b):
    return node.data == b

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
        self.end = self.head

    def toList(self):
        res = []
        pointer = self.head
        while pointer != None and pointer.data != None:
            res.append(pointer.data)
            pointer = pointer.next

        return res

    def empty(self):
        self.head = Node()
        self.size = 0
        self.end = self.head

    def appendList(self, list):

        for i in list:
            self.append(i)

    def sort(self, comparator = None):
        listStore, res = self.toList(), None
        if comparator == None:
            res = quickSort(listStore)
        else:
            res = quickSort(listStore,comparator)

        self.empty()
        self.appendList(res)


    def append(self, data):

        if self.size == 0:
            self.head.data = data
        else:
            newNode = Node(data)
            self.end.next = newNode
            self.end = newNode

        self.size += 1

    def getFirst(self, data, comparator = defaultComparator):

        pointer = Node()
        pointer.next = self.head

        while pointer.next != None:
            if pointer.next.data != None and comparator(pointer.next, data):
                return pointer.next
            pointer = pointer.next

        return None

    def removeFirst(self, data, comparator=defaultComparator):

        pointer = Node()
        pointer.next = self.head

        while pointer.next != None:
            if pointer.next.data != None and comparator(pointer.next, data):
                toBeRemoved = pointer.next
                pointer.next = toBeRemoved.next
                self.size -= 1
                if self.size == 0:
                    self.head = Node()
                    self.end = self.head
                else:
                    if toBeRemoved is self.head:
                        self.head = toBeRemoved.next
                    if toBeRemoved is self.end:
                        self.end = pointer

                return

            pointer = pointer.next


    def insertBefore (self, data, comparator = defaultComparator):
        # print("insertBefore")
        if self.head.data == None:
            self.append(data)
            return

        newNode = Node(data)
        # print(str(comparator(pointToHead,data)))
        if comparator(self.head,data):
            # print("in")
            self.head,newNode.next = newNode, self.head
            return

        prev = self.head
        while prev.next != None:
            # print(comparator(pointer, data))
            if comparator(prev.next, data):
                prev.next, newNode.next = newNode, prev.next
                return
            prev = prev.next

        self.append(data)


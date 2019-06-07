class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1

class BST:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def insert(self,data):
        self.size += 1
        if self.size == 1:
            self.root.data = data
            return

        return self.realInsert(self.root,data)

    def realInsert(self,node,data):
        if node.data == data:
            node.count += 1
            return
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
                return
            else:
                self.realInsert(node.left,data)
                return

        if node.right is None:
            node.right = Node(data)
            return

        self.realInsert(node.right,data)

    def toList(self,direction = "asc"):
        res = []
        if self.size == 0:
            return res

        if direction == "desc":
            self.visitNodeDesc(self.root, res)
        else:
            self.visitNodeAsc(self.root,res)

        return res

    def visitNodeAsc(self,node,list):
        if node == None:
            return
        self.visitNodeAsc(node.left,list)
        list += [node.data]*node.count
        self.visitNodeAsc(node.right, list)

    def visitNodeDesc(self,node,list):
        if node == None:
            return
        self.visitNodeDesc(node.right,list)
        list += [node.data]*node.count
        self.visitNodeDesc(node.left, list)

    def insertList(self,list):
        for i in list:
            self.insert(i)


    def searchNode(self,data):
        if self.root.data is None:
            return None
        return self.realSearch(self.root,data)

    def realSearch(self, node, data):

        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.realSearch(node.left, data)

        return self.realSearch(node.right, data)

    def remove(self,data):
        if self.size == 0:
            return
        else:
            self.realRemove(self.root,data)

    def realRemove(self,node,data):
        if node is None:
            return None

        if data < node.data:
            node.left = self.realRemove(node.left,data)
        elif data > node.data:
            node.right = self.realRemove(node.right, data)
        else:
            self.size -= 1

            if node.count >1 :
                node.count -= 1
                return node
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = self.findMin(node.right)
                node.data = temp.data
                node.count = temp.count
                node.right = self.realRemove(node.right,temp.data)

        return node


    def findMin(self, node):

        if node.left is None:
            return node
        else:
            return self.findMin(node.left)

from BST import BST
bst = BST()
bst.insertList([6,7,4,32,54,67,8,5,4,3,5,4,3])
bst.toList()
from LinkedList import LinkedList
from arraySortLib import defaultCompare
"""
Insert sort with linked list implementation
- O(n^2)
- using linked list here, insert elements to appropriate places.

"""
def insertionSort(arr, comparator=defaultCompare):

    def incertBeforeThisNode(node, data):
        return comparator(data, node.data)

    linkedList = LinkedList()

    for i in range(len(arr)):
        ele = arr[i]
        linkedList.insertBefore(ele, incertBeforeThisNode)
        # print(linkedList.toList())

    return linkedList.toList()


"""
Sanity test
"""
# a = [8,4,7,4,7,2,67,45,8,32,6,5,8,56]
# print(insertionSort(a))


"""
We have Node class:
    Data
    next node
    previous node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
Linked List:
    add
    remove
    search
    top:what is in the first)
    show:printing the LinkedList
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if p.data is k:
                    return p
                p = p.next
            if p.data is k:
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def show(self):
        s = []
        p = self.head
        if p is not None:
            while p.next is not None:
                s.append(str(p.data), "->")
                p = p.next
            s.append(str(p.data))
        return s

    def top(self):
        s = ""
        p = self.head
        s += p.data
        return s

"""From here"""
'''we have definition of MaxHeap!'''
##########################################################


def heapify(a):

    n = len(a) - 1
    for node in range(n/2, -1, -1):
        siftdown(a, node)
    return


# runs in log(n) time
def push_heap(a, val):

    a.append(val)
    siftup(a, len(a) - 1)
    return


# runs in log(n) time
def pop_heap(a):

    n = len(a) - 1
    swap(a, 0, n)
    maximum = a.pop(n)
    siftdown(a, 0)
    return maximum


# runs in log(n) time
def replace_key(a, node, newVal):

    curVal = a[node]
    a[node] = newVal

    if newVal > curVal:
        siftup(a, node)

    elif newVal < curVal:
        siftdown(a, node)
    return


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return


# runs in log(n) time
def siftdown(a, node):

    child = 2*node + 1
    if child > len(a) - 1:
        return

    if (child + 1 <= len(a) - 1) and (a[child+1] > a[child]):
        child += 1

    if a[node] < a[child]:
        swap(a, node, child)
        siftdown(a, child)
    else:
        return


# runs in log(n) time
def siftup(a, node):

    parent = (node - 1)/2
    if a[parent] < a[node]:
        swap(a, node, parent)

    if parent <= 0:
        return
    else:
        siftup(a, parent)





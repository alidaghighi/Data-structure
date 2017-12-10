

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
        self.child = None

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
                elif p.data is not k and p.hasChild():
                    return self.search(p.data, k)
                p = p.next
            if p.data is k:
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def show(self):
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += str(p.data) + " -> "
                p = p.next
            s += str(p.data)
        return s

    def top(self):
        s = ""
        p = self.head
        s += p.data
        return s

    def hasChild(self):
        if self.data[1] is 0:
            return None
        else:
            return True

"""
MaxHeap:
    public:
        push
        peek(Root of MaxHeap tree)
        pop
    private:
        __swap (swap nodes)
        __floatUp (nodes are going to their right place from bottom)
        __bubbleDown ( nodes are going to their right place from peek)

"""


class MaxHeap:
    def __init__(self, items):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            m = self.heap.pop()
            self.__bubbledown(1)

        elif len(self.heap) is 2:
            m = self.heap.pop()

        else:
            m = False

        return m

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.hap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)










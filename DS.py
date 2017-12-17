

"""
We have Node class:
    Data
    next node
    previous node
"""


class Node:
    def __init__(self, service,
                 car_model=None,
                 costumer_description=None,
                 agency_description=None,
                 price=None
                 ):
        self.data = service
        self.next = None
        self.prev = None
        self.child = None
        self.car_model = car_model
        self.costumer_description = costumer_description
        self.agency_description = agency_description
        self.price = price

    def __init__(self, agency_name=None
                 ):
        self.agency_name = agency_name
        self.next = None
        self.prev = None
        self.orders = MaxHeap()


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

    def add(self, data, child=None):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

        if child is not None:
            self.head.child = child

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if p.data is k:
                    return p
                elif p.data is not k and p.child is not None:
                    return p.child.search(k)
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
                s += (str(p.data))
                if p.child is not None:
                    s += (p.child.show())
                p = p.next
            s += (str(p.data))
        return s

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

    def getFlag(self):
        return self.heap[len(self.heap) - 1]
    

class Stack:
    def __init__(self):
        self.A = []

    def add(self, k):
        self.A.append(k)

    def remove(self):
        return self.A.pop()

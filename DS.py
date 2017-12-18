

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
                 price=None,
                 agency_name=None
                 ):
        self.data = service
        self.next = None
        self.prev = None
        self.child = None
        self.car_model = car_model
        self.costumer_description = costumer_description
        self.agency_description = agency_description
        self.price = price
        self.agency_name = agency_name


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
        swap (swap nodes)
        float_up (nodes are going to their right place from bottom)
        bubble_down ( nodes are going to their right place from peek)

"""


class MaxHeap:
    def __init__(self, items):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.float_up(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            m = self.heap.pop()
            self.bubble_down(1)

        elif len(self.heap) is 2:
            m = self.heap.pop()

        else:
            m = False

        return m

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.float_up(parent)

    def bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(largest)

    def get_flag(self):
        return self.heap[len(self.heap) - 1]


def _hash(_string):
    s = ''
    for i in _string:
        print(i)
        if i in '':
            s += '00'
        elif i in 'A':
            s += '01'
        elif i in 'B':
            s += '02'
        elif i in 'C':
            s += '03'
        elif i in 'D':
            s += '04'
        elif i in 'E':
            s += '05'
        elif i in 'F':
            s += '06'
        elif i in 'G':
            s += '07'
        elif i in 'H':
            s += '08'
        elif i in 'I':
            s += '09'
        elif i in 'J':
            s += '10'
        elif i in 'K':
            s += '11'
        elif i in 'L':
            s += '12'
        elif i in 'M':
            s += '13'
        elif i in 'N':
            s += '14'
        elif i in 'O':
            s += '15'
        elif i in 'P':
            s += '16'
        elif i in 'Q':
            s += '17'
        elif i in 'R':
            s += '18'
        elif i in 'S':
            s += '19'
        elif i in 'T':
            s += '20'
        elif i in 'U':
            s += '21'
        elif i in 'V':
            s += '22'
        elif i in 'W':
            s += '24'
        elif i in 'X':
            s += '25'
        elif i in 'Y':
            s += '26'
        elif i in 'Z':
            s += '27'
    return s

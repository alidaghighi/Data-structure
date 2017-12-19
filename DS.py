import time

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
        self.list = []
        self.car_model = car_model
        self.costumer_description = costumer_description
        self.agency_description = agency_description
        self.price = price
        self.agency_name = agency_name

        self.high_heap = MaxHeap()
        self.med_heap = MaxHeap()
        self.low_heap = MaxHeap()

    def __init__(self, service_name, priority_level, customer_name, agency_name):
        self.service = service_name
        self.customer = customer_name
        self.agency = agency_name
        self.priority = priority_level

        self.time = time.time() * -1


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
    
    def add_sub_service(self, sub_service_name, service_name):
        if self.search(sub_service_name) is not None:
            print('Err! already added!')
            return

        temp = Node(sub_service_name)
        p = self.search(service_name)

        if p is None:
            print('Err! check your service')

        if p.child is not None:
            p = p.child

            while p.next is not None:
                p = p.next

            p.next = temp

        else:
            p.child = temp
        
    def add_offer(self, service_name, agency_name):
        p = self.head

        while p.service_name != agency_name:
            p = p.next

        if service_name not in p.list:
            p.list.append(service_name)
        else:
            print('Already added!')

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

    def delete(self, service_name, agency_name):
        if self.head is None:
            print('Err! nothing found to delete')
            return
        p = self.head
        while p.service_name != agency_name:
            p = p.next

        if service_name in p.list:
            p.list.remove(service_name)

        else:
            print('Err! there is no such service!')

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

    def _order(self, service_name, agency_name, customer_name, priority_level):
        agency = self.search(agency_name)
        if agency is None:
            print('Err!')

        p = Node(service_name, priority_level, customer_name, agency_name)

        if priority_level == 'high':
            agency.high_heap.push(p)

        elif priority_level == 'normal':
            agency.med_heap.push(p)

        elif priority_level == 'low':
            agency.low_heap.push(p)

        else:
            print('Err!')
            
    def orders_list(self, agency_name):
        agency = self.search(agency_name)

        if agency is None:
            print('Err!')

        if agency.high_heap.__len__() == agency.med_heap.__len__() == agency.low_heap.__len__() == 0:
            print('There are no orders right now!')

        while agency.high_hap.__len__() != 0:
            print(agency.high_hap.pop())

        while agency.med_hap.__len__() != 0:
            print(agency.med_hap.pop())

        while agency.low_hap.__len__() != 0:
            print(agency.low_hap.pop())



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

    def __len__(self):
        return len(self.heap)

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
        elif self.heap[index].time > self.heap[parent].time:
            self.swap(index, parent)
            self.float_up(parent)

    def bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest].time < self.heap[left].time:
            largest = left
        if len(self.heap) > right and self.heap[largest].time < self.heap[right].time:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(largest)

"""
def _encode(_string):
    s = ''
    for i in _string:
        print(i)
        if i in '':
            s += '00 '
        elif i in 'A':
            s += '01 '
        elif i in 'B':
            s += '02 '
        elif i in 'C':
            s += '03 '
        elif i in 'D':
            s += '04 '
        elif i in 'E':
            s += '05 '
        elif i in 'F':
            s += '06 '
        elif i in 'G':
            s += '07 '
        elif i in 'H':
            s += '08 '
        elif i in 'I':
            s += '09 '
        elif i in 'J':
            s += '10 '
        elif i in 'K':
            s += '11 '
        elif i in 'L':
            s += '12 '
        elif i in 'M':
            s += '13 '
        elif i in 'N':
            s += '14 '
        elif i in 'O':
            s += '15 '
        elif i in 'P':
            s += '16 '
        elif i in 'Q':
            s += '17 '
        elif i in 'R':
            s += '18 '
        elif i in 'S':
            s += '19 '
        elif i in 'T':
            s += '20 '
        elif i in 'U':
            s += '21 '
        elif i in 'V':
            s += '22 '
        elif i in 'W':
            s += '23 '
        elif i in 'X':
            s += '24 '
        elif i in 'Y':
            s += '25 '
        elif i in 'Z':
            s += '26 '
    return s


def _decode(_string):
    s = ''
    splitted = _string.split()
    for i in splitted:
        if i in '00':
            s += ''
        elif i in '01':
            s += 'A'
        elif i in '02':
            s += 'B'
        elif i in '03':
            s += 'C'
        elif i in '04':
            s += 'D'
        elif i in '05':
            s += 'E'
        elif i in '06':
            s += 'F'
        elif i in '07':
            s += 'G'
        elif i in '08':
            s += 'H'
        elif i in '09':
            s += 'I'
        elif i in '10':
            s += 'J'
        elif i in '11':
            s += 'K'
        elif i in '12':
            s += 'L'
        elif i in '13':
            s += 'M'
        elif i in '14':
            s += 'N'
        elif i in '15':
            s += 'O'
        elif i in '16':
            s += 'P'
        elif i in '17':
            s += 'Q'
        elif i in '18':
            s += 'R'
        elif i in '19':
            s += 'S'
        elif i in '20':
            s += 'T'
        elif i in '21':
            s += 'U'
        elif i in '22':
            s += 'V'
        elif i in '23':
            s += 'W'
        elif i in '24':
            s += 'X'
        elif i in '25':
            s += 'Y'
        elif i in '26':
            s += 'Z'
    return s
"""

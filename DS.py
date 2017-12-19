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


class Node2:
    def __init__(self, service_name=None, priority_level=None, customer_name=None, agency_name=None):
        self.data = service_name
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

        p = Node2(service_name, priority_level, customer_name, agency_name)

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

    def list_agencies(self):
        p = self.head
        while p.next is not None:
            print(p.data, p.agency_name)
            p = p.next



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
    def __init__(self,):
        super().__init__()
        self.heap = [0]

    def __len__(self):
        return len(self.heap)

    def push(self, data):
        for i in data:
            self.heap.append(i)
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

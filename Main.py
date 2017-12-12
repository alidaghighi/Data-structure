"""
Main files
"""
from DS import LinkedList

l = LinkedList()
l1 = LinkedList()
l2 = LinkedList()
l.add(data='S1')
l.add(data='S2', child=l1)
l.add(data='S3')
l.add(data='S4')
l.add(data='S5')
l1.add(data='S21')
l1.add(data='S22')
l1.add(data='S23')

a = (l.search('S22'))
print(a)
print(l.show())


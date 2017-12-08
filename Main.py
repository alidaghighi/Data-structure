"""
Main files
"""
from DS import LinkedList, MaxHeap

services = LinkedList()
order = MaxHeap
while True:

    inputList = []
    _input = input(
        "For add service send 1"
        "For add subservice send 2"
        "For add offer send 3"
        "For delete service send 4"
        "For add agency send 5"
        "For see lists send 6"
        "For order send 7"
        "########################################"
    )
    print("########################################")
    inputList.__add__(_input)
    if inputList[0] is "1":
        services.add(input("Enter your service"))
        print("########################################")
    elif inputList[0] is "2":
        print("send your service that you want to add subservice")
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
    inputList.append(_input)

    if inputList[0] is "1":
        services.add(input("Enter your service"))
        print("########################################")
    elif inputList[0] is "2":
        print("send your service that you want to add subservice")
        serviceM = input("") # serviceM yani service e mafoul!
        print("send your subservice")
        subM = input("")
        serviceM = services.search(serviceM)
        if serviceM is not None:
            serviceM.child.add(subM)
        else:
            serviceM.child = LinkedList()
            serviceM.child.add(subM)
    elif inputList[0] is "3":
        print("")
    elif inputList[0] is "4":
        services.remove(input("Enter your service name"))
    elif inputList[0] is "5":
        print("")
    elif inputList[0] is "6":
        print("")
    elif inputList[0] is "7":
        print("")

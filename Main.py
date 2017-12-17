"""
Main files
"""
from DS import LinkedList, MaxHeap
import os

services = LinkedList()
order = MaxHeap
"""
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
"""
if __name__ == '__main__':

    agencies = LinkedList()
    services = LinkedList()

    print(45 * '-')
    print('Note1: Type "EXIT" when you wanted to quit.')
    print(45 * '-')
    print('Note2: Type "HELP" for allowed commands.')
    print(45 * '-')

    while True:
        inp = input('Enter a command: ').split()

        if len(inp) is 0:
            print("Wrong!")

        elif 'EXIT' in inp[0]:
            break

        elif inp[0] == 'CLEAR':
            clear = lambda: os.system('clear')

        elif 'HELP' in inp[0]:
            print(45 * '-')
            print('1. add an agency : \n\t>>> add agency <agency_name>\n', 45 * '-')
            print('2. add a service : \n\t>>> add agency <service_name>\n', 45 * '-')
            print('3. add a subservice to a service : \n\t>>> add subservice <subservice_name> to <service_name>\n', 45 * '-')
            print('4. add a service to an agency : \n\t>>> add offer <service_name> to <agency_name>\n', 45 * '-')
            print('5. list all available services : \n\t>>> list services\n', 45 * '-')
            print('6. list all services of a particular service : \n\t>>> list services from <service_name>\n', 45 * '-')
            print('7. list all agencies : \n\t>>> list agencies\n', 45 * '-')
            print('8. list all requests from an agency : \n\t>>> list orders of <agency_name>\n', 45 * '-')
            print('9. delete a service from an agency : \n\t>>> delete <service_name> from <agency_name>\n', 45 * '-')
            print('10. send a request for a service from an agency : \n\t>>> order <service_name> from <agency_name> by '
                  '<customer_name> with <immediacy_level> priority\n', 45 * '-')
            print('11. priority levels; choose one of them for sending request :\n\t1. high\n\t2. normal\n\t3. low')

        elif inp[0] == 'add':
            if inp[1] in 'service':
                try:
                    services.add_service(inp[2])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')

            elif inp[1] in 'subservice':
                try:
                    services.add_subservice3(inp[2], inp[4])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')

            elif inp[1] in 'agency':
                try:
                    agencies.add_agency(inp[2])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')

            elif inp[1] in 'offer':
                try:
                    agencies.add_offer(inp[2], inp[4])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')

            else:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        elif inp[0] == 'delete':
            try:
                agencies.delete(inp[1], inp[3])
            except:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        elif inp[0] == 'list':
            if inp[1] in '‫‪agencies‬‬':
                try:
                    agencies.list_agencies()
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')

            elif inp[1] in '‫‪services‬‬' and len(inp) > 2 and inp[2] in 'from':
                try:
                    services.list_services(inp[3])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')
                print()

            elif inp[1] in '‫‪services‬‬':
                try:
                    services.list_services()
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')
                print()

            elif inp[1] in 'orders':
                try:
                    agencies.list_orders(inp[3])
                except:
                    print('Wrong command!\nCheck out the instruction with "HELP" command.')
                    print()

            else:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        elif inp[0] == 'order':
            try:
                agencies.order(inp[1], inp[3], inp[5], inp[7])
            except:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        else:
            print('Wrong command!\nCheck out the instruction with "HELP" command.')
        print(45 * '-')
"""
Main files
"""
from DS import LinkedList, MaxHeap

order = MaxHeap
agencies = LinkedList()
services = LinkedList()

print(30 * ' ' + 20 * '*')
print('Type "exit" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Type "help" for allowed commands.')
print(30 * ' ' + 20 * '*')

while True:
    _input = input('Enter a command: ').split()
    try:
        if len(_input) is 0:
            print('Wrong!\ncheck "help" for more information!')
        elif 'exit' in _input[0]:
            break
        elif 'help' in _input[0]:
            print(30 * ' ' + 20 * '*')
            print('add an agency : \n -> add agency <agency_name>\n', 30 * ' ' + 20 * '*')
            print('add a service : \n -> add service <service_name>\n', 30 * ' ' + 20 * '*')
            print('add a subservice to a service : \n -> add subservice <subservice_name> to <service_name>\n',
                  30 * ' ' + 20 * '*')
            print('add a service to an agency : \n -> add offer <service_name> to <agency_name>\n',
                  30 * ' ' + 20 * '*')
            print("list all available services(It's not ready yet!) : \n -> list services\n", 30 * ' ' + 20 * '*')
            print("listAllServices of a particular service(It's not ready yet!)\n->list services from <service_name>\n",
                  30 * ' ' + 20 * '*')
            print("list all agencies : \n -> list agencies\n", 30 * ' ' + 20 * '*')
            print('list all requests from an agency : \n -> list orders of <agency_name>\n', 30 * ' ' + 20 * '*')
            print('delete a service from an agency : \n -> delete <service_name> from <agency_name>\n',
                  30 * ' ' + 20 * '*')
            print('send a request for a service from an agency : \n -> order <service_name> from <agency_name> by '
                  '<customer_name> with <immediacy_level> priority\n', 30 * ' ' + 20 * '*')
            print('priority levels; choose one of them for sending request :\n\t1. high\n\t2. normal\n\t3. low')

        elif _input[0] == 'add':

            if _input[1] in 'service':
                services.add(_input[2])
            elif _input[1] in 'subservice':
                services.add_sub_service(_input[2], _input[4])
            elif _input[1] in 'agency':
                agencies.add(_input[2])
            elif _input[1] in 'offer':
                agencies.add_offer(_input[2], _input[4])
            else:
                print('Wrong!\ncheck "help" for more information!')

        elif _input[0] == 'delete':
            agencies.delete(_input[1], _input[3])
        elif _input[0] == 'list':
            if _input[1] in '‫‪agencies‬‬':
                agencies.list_agencies()
            elif _input[1] in '‫‪services‬‬':
                print("It's not ready yet!")

            elif _input[1] in 'orders':
                agencies.orders_list(_input[3])
            else:
                print('Wrong!\ncheck "help" for more information!')

        elif _input[0] == 'order':
            agencies.order(_input[1], _input[3], _input[5], _input[7])
        else:
            print('Wrong!\ncheck "help" for more information!')
        print(30 * ' ' + 20 * '*')
    except:
        print('Wrong!\ncheck "help" for more information!')

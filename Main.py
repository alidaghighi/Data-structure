"""
Main files
"""
from DS import LinkedList, MaxHeap

order = MaxHeap
agencies = LinkedList()
services = LinkedList()

print(30 * ' ' + 20 * '*')
print('Note1: Type "EXIT" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Note2: Type "HELP" for allowed commands.')
print(30 * ' ' + 20 * '*')

while True:
    inp = input('Enter a command: ').split()
    try:
        if len(inp) is 0:
            print("Wrong!")
        elif 'EXIT' in inp[0]:
            break
        elif 'HELP' in inp[0]:
            print(30 * ' ' + 20 * '*')
            print('add an agency : \n -> add agency <agency_name>\n', 30 * ' ' + 20 * '*')
            print('add a service : \n -> add agency <service_name>\n', 30 * ' ' + 20 * '*')
            print('add a subservice to a service : \n -> add subservice <subservice_name> to <service_name>\n',
                  30 * ' ' + 20 * '*')
            print('add a service to an agency : \n -> add offer <service_name> to <agency_name>\n',
                  30 * ' ' + 20 * '*')
            print('list all available services : \n -> list services\n', 30 * ' ' + 20 * '*')
            print('list all services of a particular service : \n -> list services from <service_name>\n',
                  30 * ' ' + 20 * '*')
            print('list all agencies : \n -> list agencies\n', 30 * ' ' + 20 * '*')
            print('list all requests from an agency : \n -> list orders of <agency_name>\n', 30 * ' ' + 20 * '*')
            print('delete a service from an agency : \n -> delete <service_name> from <agency_name>\n',
                  30 * ' ' + 20 * '*')
            print('send a request for a service from an agency : \n -> order <service_name> from <agency_name> by '
                  '<customer_name> with <immediacy_level> priority\n', 30 * ' ' + 20 * '*')
            print('priority levels; choose one of them for sending request :\n\t1. high\n\t2. normal\n\t3. low')

        elif inp[0] == 'add':

            if inp[1] in 'service':
                services.add_service(inp[2])
            elif inp[1] in 'subservice':
                services.add_subservice3(inp[2], inp[4])
            elif inp[1] in 'agency':
                agencies.add_agency(inp[2])
            elif inp[1] in 'offer':
                agencies.add_offer(inp[2], inp[4])
            else:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        elif inp[0] == 'delete':
            agencies.delete(inp[1], inp[3])
        elif inp[0] == 'list':
            if inp[1] in '‫‪agencies‬‬':
                agencies.list_agencies()
            elif inp[1] in '‫‪services‬‬' and len(inp) > 2 and inp[2] in 'from':
                services.list_services(inp[3])

            elif inp[1] in '‫‪services‬‬':
                services.list_services()

            elif inp[1] in 'orders':
                agencies.list_orders(inp[3])
            else:
                print('Wrong command!\nCheck out the instruction with "HELP" command.')

        elif inp[0] == 'order':
            agencies.order(inp[1], inp[3], inp[5], inp[7])
        else:
            print('Wrong command!\nCheck out the instruction with "HELP" command.')
        print(30 * ' ' + 20 * '*')
    except:
        print('Wrong!\nCheck out the instruction with "HELP" command.')

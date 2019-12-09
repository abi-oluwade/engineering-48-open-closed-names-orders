def open_print_txt_file(file_name):
    try:
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            print(line.strip('\n'))

        opened_file.close() # closes the file so it can be saved/executed.
        # print(type(lines))
    except FileNotFoundError as errmssg: # the as errmsg captures the original message
        print('Check file name &/or path - file cannot be found')
        print(errmssg) # printing original error message.
        # raise # causes the error to 'break' code and stop running.

def open_print_close(file_name):
    try:
        with open(file_name, 'r') as file:                       #-with open automatically opens it and closes it.
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))

    except FileNotFoundError as error:
        print('Check your file')
        print('error')

    finally:
        print('execution done!')

# open_print_txt_file('orders.txt')
# open_print_txt_file('order2.txt')
open_print_close('orders.txt')

# print('Abi')

# except:
#     print('Error found when trying to open "order.txt"')
from names_class import *

new_users = []

opened_file =open('names.txt','r')
name_list = opened_file.readlines()
for names in name_list:
    new_users.append(NewUsers(names))
print(new_users)
opened_file.close()

new_users[0].output_text_file('info.txt',35, 'pink')

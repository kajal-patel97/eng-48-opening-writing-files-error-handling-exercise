from class_new_users import *

new_users = []

opened_file = open('name.txt', 'r')
lines = opened_file.readlines()
for line in lines:
    new_users.append(New_Users(line))
print(new_users)
opened_file.close()

new_users[3].output_text_file('username1.txt', 23, 'Blue')


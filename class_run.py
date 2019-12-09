from class_new_users import  *
from open_write_functions import *

New_Users.new_file('Users.txt')
person1 = New_Users('1. Beth')
person2 = New_Users('2. James')
person3 = New_Users('3. Scott')
person4 = New_Users('4. Sammy')
person5 = New_Users('5. Ashley')
person6 = New_Users('6. Brian')
person7 = New_Users('7. Stacey')
person8 = New_Users('8. Olivia')
person9 = New_Users('9. Mia')
person10 = New_Users('10. Jake')

write_in_txt_file('Users.txt', person1.name)
write_in_txt_file('Users.txt', person2.name)
write_in_txt_file('Users.txt', person3.name)
write_in_txt_file('Users.txt', person4.name)
write_in_txt_file('Users.txt', person5.name)
write_in_txt_file('Users.txt', person6.name)
write_in_txt_file('Users.txt', person7.name)
write_in_txt_file('Users.txt', person8.name)
write_in_txt_file('Users.txt', person9.name)
write_in_txt_file('Users.txt', person10.name)

read_txt_files('name.txt')



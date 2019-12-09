class New_Users():

    def __init__(self,name):
        self.name = name


# be able to read the txt file

    def read_txt_files(file_name):
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())

        except FileNotFoundError as error:
            print('Check if the file is created')
            print(error)

        finally:
            print('//// Programme Finished - File Shown')

# be able to write in the file
    def write_in_txt_file(file, item):
        try:
            with open(file, 'a') as file_to_write:
                file_to_write.write(item + '\n')

        except FileNotFoundError as error:
            print('Check the file and path!!!')
            print(error)

        finally:
            print('///Programme Executed -- written in file!')

# get user information (name)

    def get_name(self):
        return self.name


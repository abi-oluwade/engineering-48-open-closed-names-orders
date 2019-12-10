class NewUsers:

    def __init__(self, name):
        self.name = name


    def output_text_file(self, file_name, age, colour):
        try:
            with open(file_name, 'w+') as file_creation:
                file_creation.write(f'Name of the user is {self.name}'
                                    f'His age is{age}'
                                    f'His fav colour is {colour}.')
        finally:
            print('Execution complete')
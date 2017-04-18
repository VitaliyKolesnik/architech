from view import View
from model import Model


class Controller:
    def __init__(self, data_base):
        self.model = data_base




    def __first_controller(self):
        choice = -1
        while choice != 6:
            View.first_menu()
            try:
                choice = int(input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = input('Enter team names:\n')
                street = input('Enter score:\n')
                self.model.add_contact(name, street)
                View.success_message('Successfully added!')

            elif choice == 2:
                print(self.model.matches)

            elif choice == 3:
                self.model.save('data.txt')

            elif choice == 4:
                print('you choose')

            elif choice == 5:
                print('you choose')

        input('Press "Enter" to exit to main menu...\n')

    def __second_controller(self):
        choice = -1
        while choice !=5:
            View.second_menu()
            try:
                choice = int(input('Enter menu item"\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                print('you choose 1')
            elif choice ==2:
                print('you choose 2')
            elif choice == 3:
                print('you choose 3')
            elif choice == 4:
                print('you choose 4')
        input('Press "Enter" to exit to main menu...')


    def run(self):
        choice = -1
        while choice != 3:
            View.data_base_menu()
            try:
                choice = int(input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                self.__first_controller()

            elif choice == 2:
                self.__second_controller()
        self.model.save('data.txt')
class View:

    def displayMenu(self):
        print('Please select an option by entering a valid number below: ')
        print('1. Display contacts')
        print('2. Add contact')
        print('3. Delete contact')
        print('4. Update contact')
        print('5. Search for contact')
        print('6. Exit')
        while True:
            try:
                selected_option = int(input('> '))
            except ValueError:
                print('Please enter a number corresponding with an option listed above.')
            else:
                if selected_option < 1 or selected_option > 6:
                    print('Please enter a number corresponding with an option listed above.')
                    continue
                return selected_option

    def displayContacts(self, contacts):
        if len(contacts) == 0:
            print('There are no contacts stored!')
        else:
            for contact in contacts:
                print('First name:', contact[0])
                print('Last name:', contact[1])
                if contact != contacts[-1]:
                    print('---------------------')
        print()

    def requestNewContactInfo(self):
        print('Enter the information of your new contact:')
        first_name = input('First name: ')
        last_name = input('Last name: ')
        return first_name, last_name

    def requestContactToDelete(self):
        first_name = input('Enter the first name of the contact to delete: ')
        last_name = input('Enter the last name of the contact to delete: ')
        return first_name, last_name

    def requestContactToSearch(self):
        first_name = input('Enter the first name of the contact to search for: ')
        last_name = input('Enter the last name of the contact to search for: ')
        return first_name, last_name

    def requestContactToUpdate(self):
        first_name = input('Enter the first name of the contact to update: ')
        last_name = input('Enter the last name of the contact to update: ')
        return first_name, last_name

    def requestUpdatedContactInfo(self):
        first_name = input('Enter new first name: ')
        last_name = input('Enter new last name: ')
        return first_name, last_name

from Book import Book
from View import View

import sys

class Controller:

    def __init__(self):
        self.book = Book()
        self.view = View()

if __name__ == '__main__':
    controller = Controller()
    print('Welcome to the Contact Book application!')

    while True:
        selected_option = controller.view.displayMenu()
        if selected_option == 1:
            contacts = controller.book.retrieveContacts()
            controller.view.displayContacts(contacts)
        elif selected_option == 2:
            contact_info = controller.view.requestNewContactInfo()
            controller.book.addContact(contact_info)
        elif selected_option == 3:
            contact_to_delete = controller.view.requestContactToDelete()
            checked_contact = controller.book.searchContacts(contact_to_delete)
            if len(contact) == 0:
                print('Contact with the inputted information does not exist.')
                continue
            controller.book.deleteContact(contact_to_delete)
        elif selected_option == 4:
            contact_to_update = controller.view.requestContactToUpdate()
            contact = controller.book.searchContacts(contact_to_update)
            if len(contact) == 0:
                print('Contact with the inputted information does not exist.')
                continue
            new_info = controller.view.requestUpdatedContactInfo()
            controller.book.updateContact(contact_to_update, new_info)
        elif selected_option == 5:
            contact_info = controller.view.requestContactToSearch()
            contact = controller.book.searchContacts(contact_info)
            controller.view.displayContacts(contact)
        elif selected_option == 6:
            print('Exiting Contact Book...')
            sys.exit(0)

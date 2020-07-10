import sqlite3
from urllib.request import pathname2url

class Book:

    def __init__(self):
        """
        Establish a connection to the already existing contacts database. If no such database exists, create a new database.
        """
        self.connection = None
        self.cursor = None
        try:
            db_uri = 'file:{}?mode=rw'.format(pathname2url('contacts.db'))
            self.connection = sqlite3.connect(db_uri, uri=True)
            self.cursor = self.connection.cursor()
        except sqlite3.OperationalError:
            print("No DB found. Creating a new DB...")
            self.connection = sqlite3.connect('contacts.db')
            self.cursor = self.connection.cursor()
            self.cursor.execute('''CREATE TABLE contacts
                              (first text, last text)''')
            print("New DB created.")

    def retrieveContacts(self):
        self.cursor.execute('SELECT * FROM contacts')
        return self.cursor.fetchall()

    def addContact(self, contact_info):
        try:
            self.cursor.execute('INSERT INTO contacts VALUES (?, ?)', contact_info)
        except sqlite3.IntegrityError:
            print('Unable to save contact. This could be due to the contact already existing.')
        else:
            self.connection.commit()

    def deleteContact(self, contact):
        try:
            self.cursor.execute('DELETE FROM contacts WHERE first=? AND last=?', contact)
        except sqlite3.IntegrityError:
            print('Unable to delete contact.')
        else:
            self.connection.commit()

    def updateContact(self, contact, newInfo):
        try:
            allInfo = newInfo + contact
            print(allInfo)
            self.cursor.execute('UPDATE contacts SET first=?, last=? WHERE first=? AND last=?', allInfo)
        except sqlite3.IntegrityError:
            print('Unable to update contact.')
        else:
            self.connection.commit()

    def searchContacts(self, info):
        self.cursor.execute('SELECT * FROM contacts WHERE first=? AND last=?', info)
        return self.cursor.fetchall()

    def __del__(self):
        if self.connection is not None:
            if self.cursor is not None:
                self.cursor.close()
            self.connection.close()

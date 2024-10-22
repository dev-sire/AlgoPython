class Library:
      def __init__(self, listofbooks):
            self.availablebooks = listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   for book in self.availablebooks:
                        print(book)
                
      def removeBook(self, requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been Removed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self, returnedBook):
            self.availablebooks.append(returnedBook)
            print("Book added successfully!")

myLibrary = Library(['book1', 'book2', 'book3'])
myLibrary.addBook('book4')
myLibrary.displayAvailablebooks()
myLibrary.removeBook('book2')
myLibrary.displayAvailablebooks()
class liblary():
    def __init__(self,book_name,author):
        self.book_name=book_name
        self.author=author
        self.is_available=True
    def check_out(self):
        if self.is_available:
            self.is_available=False
            print('{} has been checked out'.format(self.book_name))
        else:
            print('sorry {} is already checked out'.format(self.book_name))
    def return_book(self):
        if not self.is_available:
            self.is_available=True
            print('{} has been returned'.format(self.book_name))
        else:
            print('{} has not checked out'.format(self.book_name))
    def display_book(self):
        status="Available" if self.is_available else "Not Available"
        print("Book name:{}".format(self.book_name))
        print("Author name:{}".format(self.author))
        print("status:{}".format(status))
        print("-"*30)
book1=liblary("Atomic habits","James clear")
book2=liblary("Art of nigotiation","vinis")
book1.display_book()
book2.display_book()
book1.check_out()
book1.display_book()
book1.return_book()
book1.display_book()
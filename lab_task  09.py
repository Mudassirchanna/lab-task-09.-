# lab_task
"""Q:no: 02 create a class named  book.
add attributes :title and author .
create a methon display_info() to display book details.
create three book objects."""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

book1 = Book("Python", "Ali")
book2 = Book("Java", "Ahmed")
book3 = Book("C++", "Sara")

book1.display_info()
book2.display_info()
book3.display_info()
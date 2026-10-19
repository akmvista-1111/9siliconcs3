class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f'Title: {self.__title}\nAuthor: {self.__author}')

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__np = number_pages

    def get_number_of_pages(self):
        return self.__np

    def set_number_of_pages(self, number_pages):
        if number_pages < 0:
            return "The number of pages must be positive."
        else:
            self.__np = number_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__in = issue_number

    def get_issue_number(self):
        return self.__in

    def set_issue_number(self, issue_number):
        if issue_number < 0:
            return "The number of issues must be positive."
        else:
            self.__in = issue_number

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("NAtional Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
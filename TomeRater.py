class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average_sum = 0
        for value in self.books.values():
            if value:
                average_sum += value
        average_rating = average_sum/len(self.books)
        return average_rating

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def add_rating(self, rating):
        if rating and 0 <= rating and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.email

    def get_average_rating(self):
        average_sum = 0
        for item in self.ratings:
            average_sum+=item
        average_rating = average_sum/len(self.ratings)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbns = []

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        if isbn in self.isbns:
            print("That ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return book

    def create_novel(self, title, author, isbn):
        book = Fiction(title, author, isbn)
        if isbn in self.isbns:
            print("That ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return book

    def create_non_fiction(self, title, subject, level, isbn):
        book = Non_Fiction(title, subject, level, isbn)
        if isbn in self.isbns:
            print("That ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return book

    def add_book_to_user(self, book, email, rating=None):
        for key,user in self.users.items():
            if user.email == email:
                user.read_book(book, rating)
                book.add_rating(rating)
                if self.books.get(book) == None:
                    self.books[book] = 1
                else:
                    self.books[book] += 1
                return user
        print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books=None):
        for key in self.users.keys():
            if key == email:
                print("That User already exists!")
        if not "@" in email:
            print("The email address of {}, is not a valid email address! Please try again".format(email))
        else:
            self.users[email] = User(name,email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)


    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        most_read_num = 0
        most_read_book = ""
        for key, value in self.books.items():
            if value > most_read_num:
                most_read_num = value
                most_read_book = key
        return most_read_book

    def highest_rated_book(self):
        highest_average_num = 0
        highest_average_book = ""
        for key in self.books:
            if key.get_average_rating() > highest_average_num:
                highest_average_num = key.get_average_rating()
                highest_average_book = key
        return highest_average_book

    def most_positive_user(self):
        highest_average_num = 0
        highest_average_user = ""
        for value in self.users.values():
            if value.get_average_rating() > highest_average_num:
                highest_average_num = value.get_average_rating()
                highest_average_user = value
        return highest_average_user
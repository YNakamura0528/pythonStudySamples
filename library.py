
def main():
    library = Library()
    library.getBook("耳をすませば")
    library.getBook("吾輩は猫である")
    library.getBook("プロを目指す人のためのRuby入門")

    library.showBooks()
    print("")

    print("なかむらが1番の本を借ります :")
    library.lendBook(1, "なかむら")
    print("")

    print("すずきが1番の本を借ります :")
    library.lendBook(1, "すずき")
    print("")

class Library():
    def __init__(self):
        self.books = {}

    def lendBook(self, bookTitle, borrowerName):
        if self.books[bookTitle].isLent():
            print("貸し出し不可です")
        else:
            print("返却予定日を入力してください : ", end = "")
            date = input()
            self.books[bookTitle].lendTo(borrowerName, date)
            print("貸出ししました")

    def returnBook(self, bookTitle):
        return self.books[bookTitle].back()

    def getBook(self, bookTitle, author = None):
        bookID = self.getUniqID()
        self.books[bookID] = Book(title = bookTitle, author = author)

    def showBooks(self):
        for bookID, book in self.books.items():
            print("{0} : {1}".format(bookID, book.title))

    def getUniqID(self):
        i = 1
        while True:
            if i in self.books:
                i += 1
            else:
                return i

class Book():
    def __init__(self, title, author = None):
        self.title = title
        self.author = author
        self.isLentTo = None
        returningDate = None

    def lendTo(self, borrowerName, returningDate):
        # 貸出中ならFalseを返す
        if self.isLent():
            return False
        # 貸出中でなければ貸出先を書き換えてTrueを返す
        else:
            self.isLentTo = borrowerName
            self.returningDate = returningDate
            return True

    def back(self):
        self.isLentoTo = None
        self.returningDate = None
        return True

    def isLent(self):
        return bool(self.isLentTo)

if __name__ == '__main__':
    main()

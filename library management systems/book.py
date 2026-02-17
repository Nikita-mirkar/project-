class Book:
    def __init__(self, bid, title, author, price, added_date):
        self.bid = bid
        self.title = title
        self.author = author
        self.price = price
        self.added_date = added_date

    def __str__(self):
        return f"{self.bid},{self.title},{self.author},{self.price},{self.added_date}"

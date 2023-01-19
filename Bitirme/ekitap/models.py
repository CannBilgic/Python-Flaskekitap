from dataclasses import dataclass
from datetime import datetime
from ekitap import db


@dataclass
class Type (db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    typeName = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, id, typeName):
        self.id = id
        self.typeName = typeName

    @classmethod
    def get_all_type(cls):
        return cls.query.all()

    @classmethod
    def get_type_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_type(cls, typeName):
        type = cls(None, typeName)
        db.session.add(type)
        db.session.commit()

    @classmethod
    def update_type(cls, typeName):
        type = cls.query.filter_by(id=id).first()
        type.typeName = typeName
        db.session.commit()

    @classmethod
    def delete_type(cls, id):
        type = cls.query.filter_by(id=id).first()
        db.session.delete(type)
        db.session.commit()



@dataclass
class Author (db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    authorName = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id, authorName):
        self.id = id
        self.authorName = authorName

    @classmethod
    def get_all_author(cls):
        return cls.query.all()

    @classmethod
    def get_author_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_author(cls, authorName):
        author = cls(None, authorName)
        db.session.add(author)
        db.session.commit()

    @classmethod
    def delete_author(cls, id):
        author = cls.query.filter_by(id=id).first()
        db.session.delete(author)
        db.session.commit()




@dataclass
class Publisher (db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    publisherName = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id, publisherName):
        self.id = id
        self.publisherName = publisherName

    @classmethod
    def get_all_publisher(cls):
        return cls.query.all()

    @classmethod
    def get_publisher_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_publisher(cls, publisherName):
        publisher = cls(None, publisherName)
        db.session.add(publisher)
        db.session.commit()

    @classmethod
    def delete_publisher(cls, id):
        publisher = cls.query.filter_by(id=id).first()
        db.session.delete(publisher)
        db.session.commit()


@dataclass
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    book_name=db.Column(db.String(40), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey(
        'type.id'), nullable=False)
    numberofPages = db.Column(db.Integer)
    ısbn = db.Column(db.Integer, unique=True)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    publisher_id = db.Column(db.Integer, db.ForeignKey(
        'publisher.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'author.id'), nullable=False)
    img = db.Column(db.String(80), nullable=False)
    summary = db.Column(db.Text)
    

    def __init__(self, id, book_name,type_id, numberofPages, ısbn, price, quantity, publisher_id, author_id, img, summary):
        self.id = id
        self.book_name=book_name
        self.type_id = type_id
        self.numberofPages = numberofPages
        self.ısbn = ısbn
        self.price = price
        self.quantity = quantity
        self.publisher_id = publisher_id
        self.author_id = author_id
        self.img = img
        self.summary = summary

    @classmethod
    def get_all_book(cls):
        allBook =db.session.query(cls,Author,Type,Publisher). \
            select_from(cls).join(Author).join(Type).join(Publisher).all()
        
        return allBook

    @classmethod
    def get_book_by_id(cls, id):
        allBook =db.session.query(cls,Author,Type,Publisher). \
            select_from(cls).join(Author).join(Type).join(Publisher).filter(cls.id==id).all()

        return allBook

    @classmethod
    def add_book(cls, type_id,book_name, numberofPages, ısbn, price, quantity, publisher_id, author_id, img, summary):
        book = cls(None,book_name, type_id, numberofPages, ısbn, price,
                   quantity, publisher_id, author_id, img, summary)
        db.session.add(book)
        db.session.commit()

    @classmethod
    def update_book(cls, id, book_name,type_id, numberofPages, ısbn, price, quantity, publisher_id, author_id, img,summary):
        book = cls.query.filter_by(id=id).first()

        book.type_id = type_id
        book.book_name=book_name
        book.numberofPages = numberofPages
        book.ısbn = ısbn
        book.price = price
        book.quantity = quantity
        book.publisher_id = publisher_id
        book.author_id = author_id
        book.img=img
        book.summary = summary
        db.session.commit()

    @classmethod
    def delete_book(cls, id):
        book = cls.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit() 

    
    


@dataclass
class Orders (db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    price = db.Column(db.Integer)

    def __init__(self, id, users_id, book_id, price):
        self.id = id
        self.users_id = users_id
        self.book_id = book_id
        self.price = price

    @classmethod
    def get_all_Orders(cls):
        return cls.query.all()

    @classmethod
    def get_Orders_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_Orders(cls, user_id, book_id, price):
        Orders = cls(None, user_id, book_id, price)
        db.session.add(Orders)
        db.session.commit()

    @classmethod
    def delete_Orders(cls, id):
        Orders = cls.query.filter_by(id=id).first()
        db.session.delete(Orders)
        db.session.commit()


@dataclass
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30))
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phonNumber = db.Column(db.String(13), unique=True)
    password = db.Column(db.String(16), nullable=False)
    coin = db.Column(db.Integer)
    authority = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200))
    orders = db.relationship('Orders')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, id, name, surname, username, email, phonNumber, password, coin, authority, address):
        self.id = id
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.phonNumber = phonNumber
        self.password = password
        self.coin = coin
        self.authority = authority
        self.address = address

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_users_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_users_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def add_users(cls, name, surname, username, email, phonNumber, password, coin, authority, address,):
        user = cls(None, name, surname, username, email,
                   phonNumber, password, coin, authority, address)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update_users(cls, id, name, surname, username, email, phonNumber, password, coin, authority, address):
        user = cls.query.filter_by(id=id).first()
        user.name = name
        user.surname = surname
        user.username = username
        user.email = email
        user.phonNumber = phonNumber
        user.password = password
        user.coin = coin
        user.authority = authority
        user.address = address
        db.session.commit()

    @classmethod
    def delete_users(cls, id):
        user = cls.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

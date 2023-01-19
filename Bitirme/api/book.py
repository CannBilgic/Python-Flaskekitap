from flask import Flask, request, jsonify, Blueprint
from ekitap.models import Book
apiBook = Blueprint('apiBook', __name__, url_prefix='/api/book')


@apiBook.route('/', methods=["GET"])
def book_list():
    try:
        allBook = Book.get_all_book()
        book = []
        for books,  author ,type , publisher in allBook:
            book.append({"id": books.id,"book_name": books.book_name,"type": type.typeName, "numberofPages": books.numberofPages,
                         "ısbn": books.ısbn, "price": books.price, "quantity": books.quantity, "publisher": publisher.publisherName, "author": author.authorName,
                         "img": books.img, "summary": books.summary})
        return jsonify(book)
    except Exception as e:

        print("Error", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiBook.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def books_delete_update_list(id):
    try:
        books = Book.get_book_by_id(id)
        if books == None:
            return jsonify({"success": False, "message": "Book not found"})
        if request.method == "GET":
            for allbook,  author ,type , publisher in books:
                bookobj=({"id": allbook.id,"book_name": allbook.book_name,"type": type.typeName, "numberofPages": allbook.numberofPages,
                         "ısbn": allbook.ısbn, "price": allbook.price, "quantity": allbook.quantity, "publisher": publisher.publisherName, "author": author.authorName,
                         "img": allbook.img, "summary": allbook.summary})


            """
            bookobj = {"id": books.id,"book_name": books.book_name, "type_id": books.type_id, "numberofPages": books.numberofPages,
                       "ısbn": books.ısbn, "price": books.price, "quantity": books.quantity, "publisher_id": books.publisher_id,
                       "author_id": books.author_id, "img": books.img, "summary": books.summary}"""
            return jsonify(bookobj)
        elif request.method == "DELETE":
            Book.delete_book(id)
            return jsonify({"success": True, "message": "Book deleted"})
        elif request.method == "PUT":
            book_name= request.form.get("book_name")
            type_id = request.form.get("type_id")
            numberofPages = request.form.get("numberofPages")
            ısbn = request.form.get("ısbn")
            price = request.form.get("price")
            quantity = request.form.get("quantity")
            publisher_id = request.form.get("publisher_id")
            author_id = request.form.get("author_id")
            img=request.form.get("img")
            summary = request.form.get("summary")
            if book_name == None:
                book_name = books.book_name
            if type_id == None:
                type_id = books.type_id
            if numberofPages == None:
                numberofPages = books.numberofPages
            if ısbn == None:
                ısbn = books.ısbn
            if price == None:
                price = books.price
            if quantity == None:
                quantity = books.quantity
            if publisher_id == None:
                publisher_id = books.publisher_id
            if author_id == None:
                author_id = books.author_id
            if img == None:
                img = books.img
            if summary == None:
                summary = books.summary
            Book.update_book(id,book_name, type_id, numberofPages, ısbn,
                             price, quantity, publisher_id, author_id,img, summary)
            return jsonify({"success": True, "message": "Book updated"})
    except Exception as e:
        print("error: ", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiBook.route('/addbook', methods=["POST"])
def addBook():
    try:
        book_name=request.form.get("book_name")
        type_id = request.form.get("type_id")
        numberofPages = request.form.get("numberofPages")
        ısbn = request.form.get("ısbn")
        price = request.form.get("price")
        quantity = request.form.get("quantity")
        publisher_id = request.form.get("publisher_id")
        author_id = request.form.get("author_id")
        img = request.form.get("img")
        summary = request.form.get("summary")
        Book.add_book(type_id,book_name, numberofPages, ısbn, price,
                      quantity, publisher_id, author_id, img, summary)
        return jsonify({"success": True, "message": "Book add a succesfully..."})
    except Exception as e:
        print("error:", e)
        return jsonify({"succes": False, "message": "There is an error..."})

from flask import Flask, request, jsonify, Blueprint
from ekitap.models import Author


apiAuthor = Blueprint('apiAuthor', __name__, url_prefix='/api/author')


@apiAuthor.route('/', methods=["GET", "POST"])
def author_list():
    try:
        allauthor = Author.get_all_author()
        authors = []
        for author in allauthor:
            authors.append({"id": author.id, "authorName": author.authorName})
        return jsonify(authors)
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiAuthor.route("/<int:id>", methods=["GET", "DELETE"])
def author_delete_list(id):
    try:
        author = Author.get_author_by_id(id)
        if type == None:
            return jsonify({"success": False, "message": "Author not found"})
        if request.method == "GET":
            authorobj = {"id": author.id, "typeName": author.authorName}
            return jsonify(authorobj)
        elif request.method == "DELETE":
            Author.delete_author(id)
            return jsonify({"success": True, "message": "Author deleted"})
    except Exception as e:
        print("Error", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiAuthor.route("/addauthor", methods=["GET", "POST"])
def addType():
    try:
        authorName = request.form.get("authorName")
        Author.add_author(authorName)
        return jsonify({"success": True, "message": "Author add a succesfully..."})
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})

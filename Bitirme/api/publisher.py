from flask import Flask, request, jsonify, Blueprint
from ekitap.models import Publisher


apiPublisher = Blueprint('apiPublisher', __name__, url_prefix='/api/publisher')


@apiPublisher.route('/', methods=["GET"])
def publisher_list():
    try:
        allpublisher = Publisher.get_all_publisher()
        publishers = []
        for publisher in allpublisher:
            publishers.append(
                {"id": publisher.id, "publisherName": publisher.publisherName})
        return jsonify(publishers)
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiPublisher.route("/<int:id>", methods=["GET", "DELETE"])
def publisher_delete_list(id):
    try:
        publisher = Publisher.get_publisher_by_id(id)
        if publisher == None:
            return jsonify({"success": False, "message": "Publisher not found"})
        if request.method == "GET":
            publisherobj = {"id": publisher.id,
                            "publisherName": publisher.publisherName}
            return jsonify(publisherobj)
        elif request.method == "DELETE":
            Publisher.delete_publisher(id)
            return jsonify({"success": True, "message": "Publisher deleted"})
    except Exception as e:
        print("Error", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiPublisher.route("/addpublisher", methods=["GET", "POST"])
def addPublisher():
    try:
        publisherName = request.form.get("publisherName")
        Publisher.add_publisher(publisherName)
        return jsonify({"success": True, "message": "Publisher add a succesfully..."})
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})

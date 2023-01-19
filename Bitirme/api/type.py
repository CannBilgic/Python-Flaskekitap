
from flask import Flask, request, jsonify, Blueprint
from ekitap.models import Type


apiType = Blueprint('apiType', __name__, url_prefix='/api/type')


@apiType.route('/', methods=["GET", "POST"])
def tpye_list():
    try:
        alltype = Type.get_all_type()
        types = []
        for type in alltype:
            types.append({"id": type.id, "typename": type.typeName})
        return jsonify(types)
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiType.route("/<int:id>", methods=["GET", "DELETE"])
def type_delete_list(id):
    try:
        type = Type.get_type_by_id(id)
        if type == None:
            return jsonify({"success": False, "message": "Type not found"})
        if request.method == "GET":
            typeobj = {"id": type.id, "typeName": type.typeName}
            return jsonify(typeobj)
        elif request.method == "DELETE":
            Type.delete_type(id)
            return jsonify({"success": True, "message": "Type deleted"})
    except Exception as e:
        print("Error", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiType.route("/addtype", methods=["GET", "POST"])
def addType():
    try:
        typeName = request.form.get("typeName")
        Type.add_type(typeName)
        return jsonify({"success": True, "message": "Type add a succesfully..."})
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "There is an error"})

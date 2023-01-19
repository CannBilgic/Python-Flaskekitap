from flask import Flask, request, jsonify, Blueprint
from ekitap.models import Orders

apiOrders = Blueprint('apiOrders', __name__, url_prefix='/api/orders')


@apiOrders. route('/', methods=["GET", "POST"])
def orders_list():
    try:
        allOrders = Orders.get_all_Orders()
        order = []
        for orders in allOrders:
            order.append({"id": orders.id, "users_id": orders.users_id,
                         "book_id": orders.book_id, "price": orders.price})
        return jsonify({"success": True, "data": order})
    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiOrders.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def orders_delete_update_list(id):

    try:
        orders = Orders.get_Orders_by_id(id)
        if orders == None:
            return jsonify({"succes": False, "message": "orders not found"})

        if request.method == "GET":
            ordersObj = {"id": orders.id, "users_id": orders.users_id,
                         "book_id": orders.book_id, "price": orders.price}
            return jsonify({"success": True, "data": ordersObj})

        elif request.method == "DELETE":
            Orders.delete_Orders(id)
            return jsonify({"succes": True, "message": "orders deleted"})

    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiOrders.route("/addorders", methods=["GET", "POST"])
def addUsers():
    try:
        users_id = request.form.get("users_id")
        book_id = request.form.get("book_id")
        price = request.form.get("price")
        Orders.add_Orders(users_id, book_id, price)
        return jsonify({"success": True, "message": "orders add a succesfully..."})
    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})

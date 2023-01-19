from ekitap import createApp
from ekitap.models import db
from api.type import apiType
from api.author import apiAuthor
from api.publisher import apiPublisher
from api.book import apiBook
from api.users import apiUsers
from api.orders import apiOrders

app = createApp()
with app.app_context():
    db.create_all()

app.register_blueprint(apiType)
app.register_blueprint(apiAuthor)
app.register_blueprint(apiPublisher)
app.register_blueprint(apiBook)
app.register_blueprint(apiUsers)
app.register_blueprint(apiOrders)




@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html"), 200


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Succesfully added the new cafe."}), 200


@app.route("/random")
def random():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(cafe=random_cafe.to_dict()), 200


@app.route("/all")
def all():
    all_cafes = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=all_cafes), 200


@app.route("/search")
def search():
    location = request.args.get("location")
    cafes = Cafe.query.filter_by(location=location).all()
    if len(cafes) == 0:
        response = jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    else:
        cafes = [cafe.to_dict() for cafe in cafes]
        response = jsonify(cafes=cafes), 200
    return response


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit() 
        response = jsonify({"Success": "Successfully updated the price."}), 200
    else:
        response = jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    return response


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            response = jsonify({"Success": "Successfully removed the cafe."}), 200
        else:
            response = jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    else:
        response = jsonify(error="Sorry, that's not allowed. Make sure you have the correct api-key."), 403
    return response


if __name__ == '__main__':
    app.run(debug=True)

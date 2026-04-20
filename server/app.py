from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database
cars = {
    "toyota": {"model": "Toyota Corolla", "year": 2020, "price": 20000},
    "honda": {"model": "Honda Civic", "year": 2021, "price": 22000},
    "bmw": {"model": "BMW X5", "year": 2022, "price": 55000},
}


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Elite Cars 🚗",
        "available_models": list(cars.keys())
    })


@app.route("/cars/<string:model>", methods=["GET"])
def get_car(model):
    model = model.lower()

    if model in cars:
        return jsonify(cars[model]), 200

    return jsonify({"error": "Car model not found"}), 404


@app.route("/cars", methods=["POST"])
def add_car():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["brand", "model", "year", "price"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    brand_key = data["brand"].lower()

    if brand_key in cars:
        return jsonify({"error": "Car brand already exists"}), 400

    cars[brand_key] = {
        "model": data["model"],
        "year": data["year"],
        "price": data["price"]
    }

    return jsonify({
        "message": "Car added successfully",
        "car": cars[brand_key]
    }), 201


@app.route("/cars/<string:model>", methods=["DELETE"])
def delete_car(model):
    model = model.lower()

    if model in cars:
        deleted_car = cars.pop(model)
        return jsonify({
            "message": f"{deleted_car['model']} deleted successfully"
        }), 200

    return jsonify({"error": "Car model not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
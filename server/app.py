from flask import Flask

app = Flask(__name__)

car_models = ["crossroads", "roadster", "summit", "voyager"]


@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


@app.route("/model/<string:model>")
@app.route("/models/<string:model>")
def show_model(model):
    if model.lower() in car_models:
        return f"Flatiron {model.title()} is in our fleet!"
    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
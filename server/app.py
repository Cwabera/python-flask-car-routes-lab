from flask import Flask

app = Flask(__name__)

models = ["crossroads", "roadster", "summit", "voyager"]

@app.route("/")
def index():
    return "Welcome to Flatiron Cars"

@app.route("/car/<string:model_name>")
def model(model_name):
    if model_name.lower() in models:
        return f"Flatiron {model_name.title()} is in our fleet!"
    return f"No models called {model_name} exists in our catalog"

if __name__ == "__main__":
    app.run(debug=True)
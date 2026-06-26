from flask import Flask

app = Flask(__name__)
# static Routes
@app.route('/')
def home():
    return "Hello Usama!"


# Dynamic Routes
@app.route("/<name>")
def user(name):
    return f"welcome{name}"


app.run(debug=True)

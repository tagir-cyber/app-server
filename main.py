from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "не hello world!"

@app.route("/get_name")
def get_name():
    return "Тагир"


if __name__ == '__main__':
    app.run()
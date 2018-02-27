from flask import Flask

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)

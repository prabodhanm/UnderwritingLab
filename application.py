from flask import Flask

app = Flask(__name__)

@app.route("/")
def sayhello():
    return "Hello World!"

@app.route("/greet")
def sayhellotoprabodhan():
    return "Hello Prabodhan!"

if __name__ == "__main__":
     app.run()
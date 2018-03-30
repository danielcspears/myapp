from flask import Flask
application = Flask(__name__)

@application.route("/", methods=["GET"])

def hello():
 return "<p>Hello world</p>"

if __name__ == "__main__":
 application.run()
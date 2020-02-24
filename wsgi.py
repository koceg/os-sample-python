from flask import Flask
from time import strftime
application = Flask(__name__)

@application.route("/")
def hello():
    return "Running s2i image ,{}".format(strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    application.run()

from flask import Flask
from time import strftime
application = Flask(__name__)

@application.route("/")
def hello():
    return "Running inside s2i namespace,{}".format(strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    application.run()

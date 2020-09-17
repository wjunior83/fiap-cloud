from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Olá Tuca, você é linda!</h1>"

if __name__ == '__main__':
    application.run()
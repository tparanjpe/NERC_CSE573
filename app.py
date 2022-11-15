from flask import *
import main
app = Flask(__name__)
# from models import trainModels, getSinglePredictions, getMultiPredictions

# @app.route('/multi_input', methods=["GET"])
# def multiTest():
#
#     return getMultiPredictions()
#
#
# @app.route('/single_input', methods=["GET"])
# def singleTest():
#
#     return getSinglePredictions()
@app.route("/")
def web():
    return render_template('index.html')

@app.route("/gethidata")
def hi_data():
    return main.hi()

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
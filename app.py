import json
import bs4

from flask import *
import os
from stanfordNer import stanford
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

@app.route("/getStanfordData", methods=['POST'])
def stanford_data():
    os.chdir('stanfordNer')
    sentence = request.get_json()

    print(sentence)
    val = stanford.stanfordData(sentence)

    os.chdir('../templates')
    # load the file
    with open("index.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, "html.parser")
    print(soup.prettify())
    for data in soup(['mark']):
        data.decompose()

    old_text = soup.find("p", {"id": "stanford-output"})
    # # insert it into the document
    # Adding content to div
    index = 0;
    for word, token in val:
        # O = #0dcaf0; I-LOC = #20c997; #fd7e14
        new_mark = soup.new_tag("mark", id=str(index))
        new_mark.string = str(word)
        if token == "O":
            new_mark['style'] = "background-color: #0dcaf0;"
        elif token == "I-LOC":
            new_mark['style'] = "background-color: #20c997;"
        else:
            new_mark['style'] = "background-color: #fd7e14"
        old_text.insert_after(new_mark)
        old_text = soup.find("mark", {"id": str(index)})
        index += 1

    # # save the file again
    with open("index.html", "w") as outf:
        outf.write(str(soup))
    # render_template("index.html")
    # app.config["TEMPLATES_AUTO_RELOAD"] = True
    os.chdir("../nltk")
    # print(os.system("python nltk_nerc.py -input "+sentence))

    return jsonify({"stanfordData": val})


if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
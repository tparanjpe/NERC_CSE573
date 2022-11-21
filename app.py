import json
import bs4
# import sys

from flask import *
import os

from Code.stanfordNer import stanford
from Code.nltkNer import nltk_nerc
from Code.bert import run
from Code.Spacy import spacyModel

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

index = 0

@app.route("/models", methods=['POST'])
def stanford_data():
    print(os.getcwd())
    os.chdir('Code/stanfordNer')
    sentence = request.get_json()

    print(sentence)
    val = stanford.stanfordData(sentence)

    os.chdir("../nltkNer")
    nltk_val = nltk_nerc.get_nltkResult(sentence)
    print(nltk_val)

    os.chdir("../bert")
    bert_val = run.bert_data(sentence)
    print(bert_val)

    os.chdir("../Spacy")
    spacy_val = spacyModel.newSpacy(sentence)
    print(spacy_val)

    os.chdir('../../templates')
    # load the file
    global soup
    with open("index.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, "html.parser")
    #print(soup.prettify())
    for data in soup(['mark']):
        data.decompose()

    parseSentence("stanford-output", val)
    parseSentence("nltk-output", nltk_val)
    parseSentence("bert-output", bert_val)
    parseSentence("spacy-output", spacy_val)
    # # insert it into the document
    # Adding content to div

    old_text = soup.find("label", {"id": "current-sentence"})
    old_text.string = str(sentence)

    # # save the file again
    with open("index.html", "w") as outf:
        outf.write(str(soup))

    os.chdir('..')
    return jsonify({"stanfordData": val})#, {"nltkData": nltk_val})


def parseSentence(model, modelOutput):
    global index
    old_text = soup.find("p", {"id": str(model)})
    print(index)
    for word, token in modelOutput:
        # O = #0dcaf0; I-LOC = #20c997; I-PER #fd7e14; I-ORG: #ffc107; other: #d63384
        new_mark = soup.new_tag("mark", id=str(index))
        new_mark.string = str(word)
        if token == "O":
            new_mark['style'] = "background-color: #0dcaf0;"
        elif token == "I-LOC" or token == "LOC":
            new_mark['style'] = "background-color: #20c997;"
        elif token == "I-PER" or token == "PER":
            new_mark['style'] = "background-color: #fd7e14;"
        elif token == "I-ORG" or token == "ORG":
            new_mark['style'] = "background-color: #ffc107;"
        else:
            new_mark['style'] = "background-color: #d63384;"
        old_text.insert_after(new_mark)
        old_text = soup.find("mark", {"id": str(index)})
        index += 1

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello, World!"
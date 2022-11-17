import json
import bs4

from flask import *
import os
from stanfordNer import stanford
from nltkNer import nltk_nerc
from bert import run

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

@app.route("/getStanfordData", methods=['POST'])
def stanford_data():
    os.chdir('stanfordNer')
    sentence = request.get_json()

    print(sentence)
    val = stanford.stanfordData(sentence)

    os.chdir("../nltkNer")
    nltk_val = nltk_nerc.get_nltkResult(sentence)
    print(nltk_val)

    # os.chdir("../bert")
    # bert_val_mod = run.token_classifier(sentence)
    # bert_val = []
    # for val in bert_val_mod:
    #     print(val)
    #     # tuple =
    #     bert_val.extend((val["word"], val["entity_group"]))
    # print(bert_val)

    os.chdir('../templates')
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
    # parseSentence("bert-output", bert_val)
    # # insert it into the document
    # Adding content to div

    # index = 0
    # for word, token in val:
    #     # O = #0dcaf0; I-LOC = #20c997; I-PER #fd7e14; I-ORG: #ffc107; other: #d63384
    #     new_mark = soup.new_tag("mark", id=str(index))
    #     new_mark.string = str(word)
    #     if token == "O":
    #         new_mark['style'] = "background-color: #0dcaf0;"
    #     elif token == "I-LOC":
    #         new_mark['style'] = "background-color: #20c997;"
    #     else:
    #         new_mark['style'] = "background-color: #fd7e14"
    #     old_text.insert_after(new_mark)
    #     old_text = soup.find("mark", {"id": str(index)})
    #     index += 1

    # # save the file again
    with open("index.html", "w") as outf:
        outf.write(str(soup))
    # render_template("index.html")
    # app.config["TEMPLATES_AUTO_RELOAD"] = True
    # os.chdir("../nltk")
    # print(os.system("python nltk_nerc.py -input "+sentence))

    return jsonify({"stanfordData": val})


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
        elif token == "I-LOC":
            new_mark['style'] = "background-color: #20c997;"
        elif token == "I-PER":
            new_mark['style'] = "background-color: #fd7e14;"
        elif token == "I-ORG":
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
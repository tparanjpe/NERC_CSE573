import spacy
import re
import os
from spacy.scorer import Scorer
from spacy.tokens import Doc
from spacy.training.example import Example

# nlp = spacy.load('en_core_web_sm')
#
# sentence = "Apple's Steve is looking at buying U.K. startup for $1 billion"
#
# doc = nlp(sentence)
#
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
#
# for token in doc:
#     print(token.text, token.lemma_, token.tag_)

# Convert CoNLL-03 to SpaCy format
# mv ./conll2003/eng.train ./conll2003/train.txt
# mv ./conll2003/eng.testa ./conll2003/dev.txt
# mv ./conll2003/eng.testb ./conll2003/test.txt
# python3 -m spacy convert -c ner -b en_core_web_sm -n 10 ./conll2003/train.txt ./conll2003
# python3 -m spacy convert -c ner -b en_core_web_sm -n 10 ./conll2003/dev.txt ./conll2003
# python3 -m spacy convert -c ner -b en_core_web_sm -n 10 ./conll2003/test.txt ./conll2003

#generate config file
#python3 -m spacy init fill-config ./base_config.cfg ./data/config.cfg

#train the model
#dev.spacy
#python3 -m spacy train data/config.cfg --output ./models/output
#test.spacy
#python3 -m spacy train data/config.cfg --output ./models/output1

#test with dev and test files
#python3 -m spacy train data/config.cfg --output ./models/output2

def newSpacy(sentence):
    trained_nlp = spacy.load('../Spacy/models/output/model-best')

    # sentence = "Apple's Steve is looking at buying U.K. startup for $1 billion"

    doc = trained_nlp(sentence)

    data = []
    for ent in doc.ents:
        data.append((ent.text, ent.label_))
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

    res = re.findall(r"[\w]+|[',-]", sentence)
    for i in res:
        if [item for item in data if i in item]:
            print(i)
        else:
            print("no "+str(i))


    return data
    # for token in doc:
    #     print(token.text, token.lemma_, token.tag_)


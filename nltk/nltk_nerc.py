import nltk
import pandas as pd
from nltk.tag import hmm
from nltk.metrics import accuracy, precision, recall
from sklearn.metrics import recall_score, precision_score
import dill
from pathlib import Path


exists = False
my_file = Path("my_hmmtagger.dill")
if my_file.is_file():
    # file exists
    exists = True
    with open('my_hmmtagger.dill', 'rb') as f:
        ner_tagger = dill.load(f)
else:
    train_df = pd.read_csv('conll2003\\engtrain.csv')
    tagged_sentences = []
    res = []
    for index, row in train_df.iterrows():
        if pd.isna(row['Token']):
            tagged_sentences.append(res)
            res = []
            continue
        else:
            myTuple = (row['Token'], row['NER'])
            res.append(myTuple)

    ner_tagger = nltk.HiddenMarkovModelTagger.train(tagged_sentences)


test_df = pd.read_csv('conll2003\\engtestb.csv')

X_input = []
expected_tags = []
for index, row in test_df.iterrows():
    if pd.isna(row['Token']):
        continue
    else:
        X_input.append(row['Token'])
        if not pd.isna(row['NER']):
            expected_tags.append(row['NER'])

# Setup a trainer with default(None) values
# And train with the data
observed_tags = []
for token in X_input:
    tagged = ner_tagger.tag(token.split())
    observed_tags.append(tagged[0][1])


print("Accuracy: " + str(accuracy(expected_tags, observed_tags)))
print("Precision " + str(precision_score(expected_tags, observed_tags, average='macro')))
print("Recall " + str(recall_score(expected_tags, observed_tags, average='macro')))

if not exists:
    with open('my_hmmtagger.dill', 'wb') as f:
        dill.dump(ner_tagger, f)

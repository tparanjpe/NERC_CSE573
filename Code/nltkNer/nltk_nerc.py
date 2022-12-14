import nltk
import pandas as pd
from nltk.tag import hmm
from nltk.metrics import accuracy, precision, recall
from sklearn.metrics import recall_score, precision_score
import dill
from pathlib import Path
import sys
import argparse




def trainModel():
    train_df = pd.read_csv('..\\Data\\conll2003\\engtrain.csv')
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

    with open('my_hmmtagger.dill', 'wb') as f:
        dill.dump(ner_tagger, f)

    return ner_tagger

def testWithConll(ner_tagger):
    test_df = pd.read_csv('..\\Data\\conll2003\\engtestb.csv')

    X_input = []
    expected_tags = []
    for index, row in test_df.iterrows():
        if pd.isna(row['Token']):
            continue
        else:
            X_input.append(row['Token'])
            if not pd.isna(row['NER']):
                expected_tags.append(row['NER'])

    observed_tags = []
    for token in X_input:
        tagged = ner_tagger.tag(token.split())
        observed_tags.append(tagged[0][1])

    getClassificationMetrics(observed_tags, expected_tags)

    
def getClassificationMetrics(observed_tags, expected_tags):
    print("Accuracy: " + str(accuracy(expected_tags, observed_tags)))
    print("Precision " + str(precision_score(expected_tags, observed_tags, average='macro')))
    print("Recall " + str(recall_score(expected_tags, observed_tags, average='macro')))

def testWithSentenceString(input_string, ner_tagger):
    tagged_results = []
    input = input_string.split()
    for token in input:
        tagged = ner_tagger.tag(token.split())
        tagged_results.append(tagged)
    
    return tagged_results

def get_nltkResult(input_string):
    my_file = Path("my_hmmtagger.dill")
    if my_file.is_file():
        # file exists
        with open('my_hmmtagger.dill', 'rb') as f:
            ner_tagger = dill.load(f)
    else:
        ner_tagger = trainModel()

    results = testWithSentenceString(input_string, ner_tagger)

    final_results = []
    for element in results:
        final_results.append(element[0])
    
    return final_results

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-input", "--input_string", help="Test input")
    args = parser.parse_args()

    given_input = args.input_string
    print(args.input_string)

    my_file = Path("my_hmmtagger.dill")
    if my_file.is_file():
        # file exists
        with open('my_hmmtagger.dill', 'rb') as f:
            ner_tagger = dill.load(f)
    else:
        ner_tagger = trainModel()

    results = testWithSentenceString(given_input, ner_tagger)

    final_results = []
    for element in results:
        final_results.append(element[0])

    print(final_results)

if __name__ == "__main__":
    main()











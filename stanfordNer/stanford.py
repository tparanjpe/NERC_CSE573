# before running,
# 1. pip install NLTK
# engtrain.txt is the training data separated by tab
# training_stanford is test a data (confusing name...need to change)
# english.all.3class.distsim.prop is what trains the model 
# run command java -classpath stanford-ner.jar -mx4g edu.stanford.nlp.ie.crf.CRFClassifier -prop .\english.all.3class.distsim.prop   to train
# run command java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile .\training_stanford.txt  to test and get accuracy 

import nltk 
# 
from nltk.tag.stanford import StanfordNERTagger
import os
import subprocess
from typing import List

def stanfordData(sentence):
    # "C:\Users\mayak\OneDrive\Documents\CSE 573\NERC_CSE573\stanford-postagger-full-2020-11-17\models\english-left3words-distsim.tagger.props"
    # Need Java for this package
    java_path = "C:/Program Files/Java/jdk1.8.0_181/bin/java.exe"
    os.environ['JAVAHOME'] = java_path
    os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk1.8.0_181'


    # sentence = u"Twenty miles east of Reno, Nev., " \
    #     "where packs of wild mustangs roam free through " \
    #     "the parched landscape, Tesla Gigafactory 1 " \
    #     "sprawls near Interstate 80."

    jar = 'stanford-ner.jar'
    model = 'ner-model.ser.gz'

    # Prepare NER tagger with english model
    ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

    # Tokenize: Split sentence into words
    words = nltk.word_tokenize(sentence)

    # Run NER tagger on words
    print(ner_tagger.tag(words))
    return ner_tagger.tag(words)

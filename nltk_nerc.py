import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tag import hmm
from nltk.corpus import treebank

# Train data - pretagged
train_data = treebank.tagged_sents()[:4000]

tagger = nltk.HiddenMarkovModelTagger.train(train_data)
print(tagger)
print(tagger.tag("Today is a good day .".split()))


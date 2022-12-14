from transformers import pipeline

model_checkpoint = "classtest/berttest2"
token_classifier = pipeline(
    "token-classification", model=model_checkpoint, aggregation_strategy="simple"
)

def bert_data(example_string):
    #use any input
    # example_string = "Apple's Steve is looking at buying U.K. startup for $1 billion"
    example_list = example_string.split(" ")

    classification = token_classifier(example_string)

    classified = {}
    for i in classification:
        word = i["word"].replace(' ', '')
        classified[word] =  i["entity_group"]

    final = []
    for i in example_list:
        done = False
        for k in classified.keys():
            if k in i:
                final.append((i, classified[k]))
                done = True
        if done is False:
            final.append((i, "O"))

    #print(final)
    return final

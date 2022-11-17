from transformers import pipeline

model_checkpoint = "classtest/berttest2"
token_classifier = pipeline(
    "token-classification", model=model_checkpoint, aggregation_strategy="simple"
)

#use any input
print(token_classifier("My name is Rifa and I study at Arizona State University."))
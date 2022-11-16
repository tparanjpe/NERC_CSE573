---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: berttest2
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9137532981530343
    - name: Recall
      type: recall
      value: 0.932514304947829
    - name: F1
      type: f1
      value: 0.9230384807596203
    - name: Accuracy
      type: accuracy
      value: 0.9822805674927886
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# berttest2

Pytorch file is too big - can be found at model link

Model link: https://huggingface.co/classtest/berttest2

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0674
- Precision: 0.9138
- Recall: 0.9325
- F1: 0.9230
- Accuracy: 0.9823

## Model description

Model created for CSE 573 Course Project on NER
Tutorial followed for creating this model: https://huggingface.co/course/chapter7/2


## Intended uses & limitations

pip install transformers
pip install torch


Sample code in run.py

from transformers import pipeline

model_checkpoint = "classtest/berttest2"
token_classifier = pipeline(
    "token-classification", model=model_checkpoint, aggregation_strategy="simple"
)

token_classifier("My name is Rifa and I study at Arizona State University.")


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0869        | 1.0   | 1756 | 0.0674          | 0.9138    | 0.9325 | 0.9230 | 0.9823   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cpu
- Datasets 2.6.1
- Tokenizers 0.13.2

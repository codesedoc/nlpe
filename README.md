# NLPE
**N**ural **L**anguage **P**rocess **E**xperiments (NLPE) is a python package supporting you setup NLP experiments fastly.

Its mission is tio reduce the duplicate labors when we set up and NLP models or framework in current popular deep learning framework or methodology.

## Installation
### Install from Source
```
git clone https://github.com/codesedoc/nlpe.git
cd nlpe
pip install -e .
```
### Install from PyPi
```
pip install nlpe
```
### Install from Docker Hub
```
docker run -it codedocx/nlpe
```

## Experiment
There are examples of conducting expeirments by using nlpe at **experiment** dir.
The **experiment/semantic_similarity** is an example to calculate semantic similarity of two texts by fine-tuned the uncased [BERT](https://huggingface.co/google-bert/bert-base-uncased) on [STSB](https://huggingface.co/datasets/nyu-mll/glue) dataset.
```
cd experiment/semantic_similarity
pip install -r re
python main.py -t sematic_similarity -d glue -a bert --eval_strategy epoch --output_dir tmp_trainer
```
> **Version: 0.0.2**
> 
> **E-mail: gocodedoc@gmail.com** 
> 

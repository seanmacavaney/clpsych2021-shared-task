# CLPsych 2021 Shared Task - Practice Dataset

## Off the Enclave

To use the practice data outside of the enclave, you need to fetch the tweet text.

Install dependencies:

```
pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
pip install tqdm
```

Run on both the train and test sets (this will take some time):

```
python hydrate.py train.dehydrated.jsonl train.jsonl
python hydrate.py test.dehydrated.jsonl test.jsonl
```

## On the Enclave

Data are available in a hydrated form.

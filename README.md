# NLU_Debias
## Env setup
```
    pip install -U gensim
    pip3 install nltk
    pip install bert-serving
    pip install bert-serving-client
    pip install progressbar
    python3 -m pip install scikit-learn
    pip install jieba
    pip install matplotlib
    pip install fairseq
    pip install tensorboardX
    pip install -U spacy
    python -m spacy download en_core_web_sm

```
## Download GLOVE vectors, change to w2v format
Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download)

`wget https://nlp.stanford.edu/data/glove.840B.300d.zip` 

`unzip ./glove.840B.300d.zip`

According to [ref](https://radimrehurek.com/gensim/scripts/glove2word2vec.html),
**In order to make sure the KeyedVectors.load_word2vec_format() works, use this linux terminal command to add to the first line in place: '#Tokens #Dimension' to the .txt file**
```
sed -i '1i 2196017 300' glove.840B.300d.txt 
```

## Dataset
**Twitter**:
```
Total: 2175 lines
    |--- train_examples: 1631(74.99%)
    |--- dev_examples: 272(12.51%)
    |--- test_examples: 272(12.51%)
```

**Yelp_Hotel**
```
Total: 34959 lines
    |--- train_examples: 20975(60%)
    |--- dev_examples: 6991(20%)
    |--- test_examples: 6991(20%)
```

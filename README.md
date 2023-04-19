# NLU_Debias
## environment setup
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
```
## download the GLOVE data
Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download)

`wget https://nlp.stanford.edu/data/glove.840B.300d.zip` 

`unzip ./glove.840B.300d.zip`

**use this linux terminal command to add to the first line: '#Tokens #Dimension' to the .txt file**
```
  sed -i '1i 2196017 300' glove.840B.300d.txt 
```
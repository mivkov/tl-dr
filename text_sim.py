import nltk, string
import numpy as np
import re, os
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
stopwords = nltk.corpus.stopwords.words('english')

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words=stopwords)

def cosine_sim(text1, text2):
    lent1 = len(text1) 
    text = text1 + text2
    tfidf = vectorizer.fit_transform(text)
    vec =  ((tfidf * tfidf.T).A)
    cng = np.delete(np.delete(vec, np.s_[0:lent1], axis=1), np.s_[lent1:len(text)], axis=0)
    return [(text1[i],np.amax(cng[i])) for i in range(len(cng))]

def sort_pattern(x):
    return x[1]

def find_uncanny(text1, text2):
    for k in text1:
        if len(k) < 10:
            text1.remove(k)
    for k in text2:
        if len(k) < 10:
            text2.remove(k)
    res = cosine_sim(text1, text2)
    dc = {}
    for (r1, r2) in res:
        dc[r1] = r2
    return dc

def clean_sentence(dct, s):
    fs = s.replace("\n","")
    fs = re.sub(r"[0-9]+", "", fs)
    fs = re.sub(r" +", " ", fs) 
    dct[fs] = s
    return fs

def parse(f1):
    dct = {}
    text1 = list(map(lambda s: clean_sentence(dct, s), nltk.sent_tokenize(f1)))
    reg = re.compile(r"http\S+|HTTP\S+")
    for st in text1:
        if reg.search(st):
            text1.remove(st)

    maxima = {}
    path = os.getcwd()
    for root, _, files in os.walk(path + '/licenses'):
        for file in files:
            if file.endswith(".txt") and file != 'apple_fixed.txt':
                with open(os.path.join(root,file), 'r') as f:
                    text2 = list(map(lambda s: s.replace("\n",""), nltk.sent_tokenize(f.read())))
                    uncanny = find_uncanny(text1, text2)
                    for key in uncanny:
                        if key in maxima:
                            maxima[key] = max(uncanny[key],maxima[key])
                        else:
                            maxima[key] = uncanny[key]

    fin = []
    for key in maxima:
        if abs(maxima[key]-1) > 10.0**(-6):
            fin.append((key, maxima[key]))
    fin.sort(key = sort_pattern)
    if len(fin) == 0:
        return "Nothing out of the normal here!"
    else:
        return '\n'.join([dct[f[0]] for f in fin][:min(5, len(fin))])

    

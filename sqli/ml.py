from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
import numpy as np
from collections import Counter
nltk.download('stopwords')
nltk.download('wordnet')

stop = set(stopwords.words('english'))
stop.remove(('or'))
stop.remove(('from'))
stop.remove(('into'))
stop.remove(('where'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

# Cleaning the text sentences so that punctuation marks, stop words & digits are removed
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    # punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in stop_free.split())
    # processed = re.sub(r"\d+","",normalized)
    y = normalized.split()
    print(y)
    return y


print("There are 10 sentences of following three classes on which K-NN classification and K-means clustering"
      " is performed : \n1. Cricket \n2. Artificial Intelligence \n3. Chemistry")
path = "Sentences.txt"

train_clean_sentences = []
fp = open(path,'r')
for line in fp:
    line = line.strip()
    cleaned = clean(line)
    cleaned = ' '.join(cleaned)
    train_clean_sentences.append(cleaned)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(train_clean_sentences)

# Creating true labels for 30 training sentences
y_train = np.zeros(30)
y_train[10:30] = 1

# Clustering the document with KNN classifier
modelknn = KNeighborsClassifier(n_neighbors=5)
modelknn.fit(X,y_train)

# Clustering the training 30 sentences with K-means technique
modelkmeans = KMeans(n_clusters=2, init='k-means++', max_iter=200, n_init=100)
modelkmeans.fit(X)


test_sentences = ["'abc'='abc'--", \
                  "table test", \
                  "union insert into"]

test_clean_sentence = []
for test in test_sentences:
    cleaned_test = clean(test)
    cleaned = ' '.join(cleaned_test)
    # cleaned = re.sub(r"\d+","",cleaned)
    test_clean_sentence.append(cleaned)

Test = vectorizer.transform(test_clean_sentence)

predicted_labels_kmeans = modelkmeans.predict(Test)

print("\n-------------------------------PREDICTIONS BY K-Means--------------------------------------")
print("\nIndex of bool cluster : ", Counter(modelkmeans.labels_[0:10]).most_common(1)[0][0])
print("Index of union cluster : ", Counter(modelkmeans.labels_[10:30]).most_common(1)[0][0])

print("\n", test_sentences[0], ":", predicted_labels_kmeans[0],
      "\n", test_sentences[1], ":", predicted_labels_kmeans[1],
      "\n", test_sentences[2], ":", predicted_labels_kmeans[2])

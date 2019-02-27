import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
nltk.download('stopwords')

documents = ["or 123=123",
             "or '@@'='@@'",
             "or 'rishi'='rishi'",
             "or '::'='::'",
             "or '#$%'='#$%'",
             "or '98654'='98654'",
             "or '  '='  ''",
             "or 18790=18790",
             "or '!@#$%^&*9'='!@#$%^&*9'",
             "or 1234567890=1234567890",
             "drop truncate delete insert from where select into drop where",
             "union select insert union where select from drop select where insert drop into from delete",
             "union modify drop select union from select into insert drop truncate ",
             "union select union where from insert into drop truncate where union delete select from insert drop",
             "union  where select insert drop truncate delete union where truncate delete select from",
             "union select union where drop truncate delete from where insert select into delete where",
             "union select where from delete truncate drop where insert into select from",
             "select from insert into delete where drop select union delete where truncate",
             "union select where from insert into drop where delete truncate from into",
             "select from insert where into drop delete where truncate",
             "union select where from insert into where drop insert drop into where insert from insert",
             "union insert into where select from select where insert into drop insert into drop",
             "union drop where select from select insert into select where insert into drop insert",
             "union insert into where select from select into select from where insert into drop from",
             "union where update from select where insert select from drop where select insert drop into from",
             "union modify where drop select from select where into insert from where select insert drop from",
             "union select where from insert into select from select drop insert select where insert from into",
             "union insert where into select from select insert into select insert drop insert from inot",
             "union modify select from select insert drop select from drop insert from into drop",
             "union select from select from select select insert from into drop  insert into"
             ]
stop = set(stopwords.words('english'))
stop.remove(('or'))
stop.remove(('from'))
stop.remove(('into'))
stop.remove(('where'))
vectorizer = TfidfVectorizer(stop)
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=300, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")
first_test="union select from rishi where username=rak."
Y = vectorizer.transform([first_test])
prediction = model.predict(Y)
if("union" in first_test):
    print(first_test," :","union attack",prediction)
elif("or" in first_test):
    print(first_test," :","boolean attack",prediction)
else:
    print(first_test," :","piggy attack",prediction)


second_test="or '#&'='#&'."
Y = vectorizer.transform([second_test])
prediction = model.predict(Y)
prediction = model.predict(Y)
if("union" in second_test):
    print(second_test," :","union attack",prediction)
elif("or" in second_test):
    print(second_test," :","boolean attack",prediction)
else:
    print(second_test," :","piggy attack",prediction)


third_test="insert into table"
Y = vectorizer.transform([third_test])
prediction = model.predict(Y)
prediction = model.predict(Y)
if("union" in third_test):
    print(third_test," :","union attack",prediction)
elif("or" in third_test):
    print(third_test," :","boolean attack",prediction)
else:
    print(third_test," :","piggy attack",prediction)

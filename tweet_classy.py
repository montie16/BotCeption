from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

c1 = NaiveBayesClassifier(train)

print(c1.classify("Their Burgers are amazing."))
print(c1.classify("I hate their pizza."))

blob = TextBlob("The beer was amazing, but the hangover was horrible."
                    "my boss was not please.", classifier=c1)
                    
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
    
print("The Accuracy: {0}".format(c1.accuracy(test)))

c1.show_informative_features(10)
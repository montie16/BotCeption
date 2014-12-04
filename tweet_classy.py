from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I want to eat','pos'),
    ('Hanging out with friends','pos'),
    ('Had a wonderful night out last night','pos'),
    ('Their food was amazing','pos'),
    ('I do not like this restaurant', 'neg'),
    ('Breaking news come check out http:/','neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('Check out this wepage','neg'),
    ('Check out these photos','neg'),
    ('Lose weight fast','neg'),
    ('Listen to my','neg'),
    ('Follow this link','neg'),
    ('My boss is horrible.', 'neg'),
    ('Check out these celebrities','neg'),
    ('Hello World!','neg'),
    ('Hows the day going','pos'),
    ('would you care to hear some special deals','neg'),
    ('The new Iphone sucks','pos'),
    ('I love my android phone', 'pos'),
    ('Ferguson case','pos'),
    ('Hey boys wanna know a secret','neg'),
    ('Find out the top sexy models','neg'),
    ('Check this link for lovely looking ladies','neg'),
    ('This is where you go to lose weight','neg'),
    ('I was able to add weight to my lift','pos'),
    ('RT @username: ','neg'),
    ('#holla #Ferguson #cool','pos'),
    ('Adorable pic.twitter.com','neg'),
    ('pic.twitter.com','neg'),
    ('Kenny Hill be like pic.twitter.com','pos'),
    ('Did you see the football game last week?','pos'),
    ('Did you see the football game last night?','pos'),
    ('Did you see the football game?','pos'),
    ('Find out what your look alike celebrity is','neg'),
    ('Did you see the look on their faces #priceless','pos'),
    ('Interrupt my sleep and Ill Interrupt your breathing','neg'),
    ('@username want to go play soccer tonight','pos'),
    ('@username wanna go shoot some hoops','pos'),
    ('Whoop','pos'),
    ('Are people really this stupid?','pos'),
    ('Found out how you can get followers now','neg'),
    ('Come to this link to see Real celebrities lose weight fast, and how they did it','neg'),
    ('#deal','neg'),
    ('#sale','neg'),
    ('#sexyimage','neg'),
    ('#sexylook','neg'),
    ('Save big with us today','neg'),
    ('Lifted so much weight today','pos'),
    ('Squatted so much weight today','pos'),
    ('Love me some Leg Days','pos'),
    ('I love my Girlfriend','pos'),
    ('I love my Boyfriend','pos'),
    ('I love to eat so much food','pos'),
    ('Merry Christmas to everyone','pos'),
    ('Hope you have a wonderful day today, because I am','pos'),
    ('I hate when people ignore me','pos')
]
test = [
    ('The beer was good.', 'pos'),
    ('I got so turnt', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg'),
    ('I want to eat Pancakes','pos'),
    ('Listen to my live stream','neg'),
    ('Great hanging out with my friends','pos'),
    ('Hey man you wanna go kick the ball around?','pos'),
    ('Aggie football was crazy lasy week','pos'),
    ('Check out this celebrities fast weight loss','neg'),
    ('check out how cute this puppy is pic.twitter.com','neg'),
    ('Found out I am getting a Bike for Christmass','pos'),
    ('This is so Adorable pic.twitter.com','neg'),
    ('hello world','neg'),
    ('Wanna know the secret to looking sexier in just 30 days?','neg'),
    ('5 Steps to gain followers quickly','neg')
]

c1 = NaiveBayesClassifier(train)

print(c1.classify("I went out with friends last night"))
print(c1.classify("How to lose weight."))
print(c1.classify("Lose weight fast"))

blob = TextBlob("Check out this website, it can show you how to lose weight "
                    "while eating pancakes.", classifier=c1)
                    
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
    
print("The Accuracy: {0}".format(c1.accuracy(test)))

c1.show_informative_features(5)
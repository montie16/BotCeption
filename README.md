Howdy! Please ensure that python is fully updated on the machine running this code and that the TextBlob Libraries are fully installed.

To run our Tweet Based Text Classifier please enter this command:
python tweet_class.py

We have replaced the twitter user dump program with one that does not require each individual users tokens and keys, the only drawback is that now we can only pull up to 200 tweets instead of 3200, but that should still be sufficient to analyze a users account. This will also run on Python2.7.8 and does not require and additional packages from the ones we used for this class.
  
This will be able to be used with any user account once logged in through our website.
The website has been added to this github, because this Will be our page used to display botor not message.

With our final Commit we use our classifier which was hand typed at 750 training data and 75 testing data where neg will return bot and pos will be a human based tweet, you can uncomment 

#stuff = raw_input('please type in Tweet
#blob = TextBlob(stuff,classifier=c1)

This will allow any user to input a tweet and then with the Accuracy of 85% will be able to judge wheater a tweet is either a human related or bot related

You must have Tweepy installed for our Feedparser.py
Must have both TextBlot and NLTK for oru tweet_class.py

pip install -U textblob
python -m textblob.download_corpora

Our UI wasnt able to draw in our python script, because we used people.tamu.edu and it didnt work with PHP or JQuery

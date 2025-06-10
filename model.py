from textblob import TextBlob

def autocorrect(text):
    return str(TextBlob(text).correct())

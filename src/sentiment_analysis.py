import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiments(reviews):
    sentiments = []
    for review in reviews:
        polarity_scores = sia.polarity_scores(review)
        sentiments.append(polarity_scores['compound'])
    return sentiments

# Example usage
if __name__ == "__main__":
    reviews = ["This product is great!", "I didn't like this product."]
    sentiments = analyze_sentiments(reviews)
    print(sentiments)

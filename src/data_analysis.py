import pandas as pd

def analyze_data(sentiments):
    df = pd.DataFrame({'Sentiment': sentiments})
    print(df.describe())

# Example usage
if __name__ == "__main__":
    sentiments = [0.5, -0.2, 0.1, 0.9]
    analyze_data(sentiments)

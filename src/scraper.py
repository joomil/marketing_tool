import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = soup.find_all(class_='review-text')  # Adjust class name as per the target website
    return [review.text for review in reviews]

# Example usage
if __name__ == "__main__":
    url = "http://example.com/product-reviews"
    reviews = scrape_reviews(url)
    print(reviews)

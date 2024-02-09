# EXPLAINATION: this is a program that summarize news headlines using a webscraper

# Pseudocode

# import needed libraries
import requests
from bs4 import BeautifulSoup

# Provide the link for the news website that would be webscraped
url = 'https://www.philstar.com/'

# get request
response = requests.get(url)
# Create an empty list for the website headlines so it will serve as a holder for the headlines
headlines = []
# parse html
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    headline_tags = soup.find_all('h2', limit=3) 

# Extract and print the headlines
for i, tag in enumerate(headline_tags, start=1):
    headline = tag.find('a') # the Philstar headline is located in the <a> tag so i used "a" to find it.
    if headline:
        text = headline.text.strip()
    else:
        text = tag.text.strip()  
        headlines.append(text)
    print(f"Headline {i}: {text}")
else:
    print("Webpage not found")
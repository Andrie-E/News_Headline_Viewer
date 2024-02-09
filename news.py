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
        headline_link = tag.find('a') # the Philstar headline is located in the <a> tag so i used "a" to find it.
        if headline_link:
            article_url = headline_link.get('href')
            # Ensure the URL is absolute
            if article_url.startswith('/'):
                article_url = 'https://www.philstar.com' + article_url
            
# new modification: Get the 1st paragraph of the headline as a preview of the story.

            # Get the article page
            article_response = requests.get(article_url)
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, 'html.parser')
                first_paragraph = article_soup.find('p') # The Philstar 1st parag is located in the <p> tag so i used "p" to find it.
                if first_paragraph:
                    print(f"Headline {i}: {headline_link.text.strip()}")
                    print(f"URL: {article_url}")
                    print(f"Preview: {first_paragraph.text.strip()}\n")
                    
                else:
                    print(f"Headline {i}: {headline_link.text.strip()}")
                    print(f"URL: {article_url}")
                    print("Preview: the preview for this article is currently unavailable.\n")
                    
            else:
                print(f"Cannot find the Headline {i}")
        else:
            print(f"Headline {i}: unable to access this information")
else:
    print("Webpage cannot be found try again later.")
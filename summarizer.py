import newspaper
import requests
from bs4 import BeautifulSoup

# Make a GET request to the Wikipedia page to retrieve the HTML
URL = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(URL)
html = response.text

# Use Beautiful Soup to extract the main body of text from the HTML
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

# Use newspaper to summarize the text
article = newspaper.Article(url=URL, language="en")
article.set_html(text)
article.parse()
article.nlp()

# Use the LsaSummarizer to summarize the text
article.summarizer = newspaper.LsaSummarizer()
summary = article.summary

# Print the summary
print(summary)

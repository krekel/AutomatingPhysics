import requests
from bs4 import BeautifulSoup
import re


def main():
    url = "http://fisica.uprb.edu/cursos/FISI3011KH1/"
    page = make_request(url)

    # Download class presentation
    soup = BeautifulSoup(page.content, "html.parser")
    presentations = [pdf.get("href") for pdf in soup.find_all('a')]
    print(presentations)


def make_request(url):
    content = requests.get(url)
    return content

if __name__ == "__main__":
    main()

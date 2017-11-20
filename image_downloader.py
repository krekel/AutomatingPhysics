import requests
from bs4 import BeautifulSoup
import os
import re

URL = "http://fisica.uprb.edu/cursos/FISI3011KH1/problemas/"
PATH = "/Users/luis-a7x/Desktop/Physics/Problems/"
PATTERN = r'^\d{0,2}'


def create_session():
    session = requests.session()
    return session


def image_scraper(session):
    """ Retrieves the names of all the images. """
    response = session.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    # Return all the names of the images stored in the problems file
    names = [link.get("href") for link in soup.find_all('a')[5:]]
    return names


def save_image(filename, session):

    directories = create_directories(filename)

    for x in filename:
        curr_chapter = re.match(PATTERN, x).group()

        # Download Image
        content = session.get(URL+x)
        n_path = os.path.join(PATH, directories[curr_chapter])
        n_path += x

        # Save image
        with open(n_path, "wb") as f:
            f.write(content.content)


def create_directories(filename):
    dir_name = "Chapter_"
    directories = {}

    for name in filename:
        chapter_number = re.match(PATTERN, name).group()
        if chapter_number not in directories.keys():
            directories[chapter_number] = dir_name + chapter_number + "/"
            os.makedirs(PATH+directories[chapter_number])

    return directories


if __name__ == "__main__":
    s = create_session()
    f_name = image_scraper(s)
    save_image(f_name, s)

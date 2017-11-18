import requests
from bs4 import BeautifulSoup
import os
import re


def create_session():
    session = requests.session()
    return session


def image_scraper(session, url):
    """ Retrieves the name of all the images in the file. """
    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Return all the names of the images stored in the problems file
    names = [link.get("href") for link in soup.find_all('a')[5:]]
    return names


def save_image(filename, path, url, directories, pattern, session):
    for x in filename:
        curr_chapter = re.match(pattern, x).group()

        # Download Image
        content = session.get(url+x)
        n_path = os.path.join(path, directories[curr_chapter])
        n_path += x

        # Save image
        with open(n_path, "wb") as f:
            f.write(content.content)


def create_directories(filename, path, pattern):
    dir_name = "Chapter_"
    directories = {}

    for name in filename:
        chapter_number = re.match(pattern, name).group()
        if chapter_number not in directories.keys():
            directories[chapter_number] = dir_name + chapter_number + "/"
            os.makedirs(path+directories[chapter_number])

    return directories


def main():
    path = "/Users/luis-a7x/Desktop/Physics/Problems/"
    url = "http://fisica.uprb.edu/cursos/FISI3011KH1/problemas/"
    pattern = r'^\d{0,2}'

    session = create_session()
    filename = image_scraper(session, url)
    directories = create_directories(filename, path, pattern)
    save_image(filename, path, url, directories, pattern, session)

if __name__ == "__main__":
    main()

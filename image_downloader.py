import requests
from bs4 import BeautifulSoup
import os
import time
import re


def make_request(url):
    response = requests.get(url, stream=True)
    return response


def image_scraper(content):
    """ Retrieves the name of all the images in the file. """
    soup = BeautifulSoup(content, "html.parser")
    # Return all the names of the images stored in the problems file
    names = [link.get("href") for link in soup.find_all('a')[5:]]
    return names


def save_image(filename, path, url, directories, pattern):

    for k, v in directories.items():
        n_path = path + v
        curr_match = k

        for name in filename:
            chapter_number = re.match(pattern, name).group()
            if chapter_number == curr_match:
                content = make_request(url+name)   # Get image
                path = os.path.join(n_path, name)  # Adds the filename to the path
                with open(path, "wb") as f:
                    for image in content.iter_content(chunk_size=5000):
                        f.write(image)
            else:
                break
            time.sleep(0.5)


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

    response = make_request(url)
    filename = image_scraper(response.content)
    directories = create_directories(filename, path, pattern)
    save_image(filename, path, url, directories, pattern)

if __name__ == "__main__":
    main()

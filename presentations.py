import requests
from bs4 import BeautifulSoup
import re
import os


PATH = "/Users/luis-a7x/Desktop/Physics/Presentations/"
URL = "http://fisica.uprb.edu/cursos/FISI3011KH1/"


def download_pdf(url, path):
    pattern = r'([\S])+\.(pdf)'

    page = make_request(url)
    soup = BeautifulSoup(page.content, "html.parser")
    names_of_files = [re.match(pattern, pdf.get("href")).group()
                      for pdf in soup.find_all('a') if re.match(pattern, pdf.get("href"))]

    saved_files = os.listdir(path)
    files_to_download = list(set(names_of_files) - set(saved_files))

    if files_to_download:
        for file in files_to_download:
            session = make_request(url+file, session=True)
            if session.status_code == 200:
                with open(path+file, 'wb') as f:
                    f.write(session.content)
        print("New files added")


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Directory exists")


def make_request(url, session=False):
    if session:
        r = requests.session().get(url)
    else:
        r = requests.get(url)
    return r

if __name__ == "__main__":
    create_folder(PATH)
    download_pdf(URL, PATH)

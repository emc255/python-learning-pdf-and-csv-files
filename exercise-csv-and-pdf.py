import re

import PyPDF2
import gdown
import pandas as pd


def scan_phone_number():
    link = extract_hidden_link()
    file_path = save_pdf(link)
    scan_file(file_path)


def extract_hidden_link():
    data_frame = pd.read_csv("resources/files/Exercise_Files/find_the_link.csv")
    link = ""
    first_run = True
    for index, row in data_frame.iterrows():
        for i, (k, v) in enumerate(row.items()):
            if first_run:
                link += str(k)
                link += row.get(i + 1)
                first_run = False
                break
            if index == i - 1:
                link += str(v)
                break
    return link


def save_pdf(link: str):
    file_path = "resources/files/Exercise_Files/pdf/business-deliverables.pdf"
    # business-deliverables-v2 is back up in case the link is gone
    # in Google Drive the link in downloading should be UC
    # https://drive.google.com/uc?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q
    # https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q < link provided
    # convert open to uc
    # once converted  no need to use the fuzzy
    link = link.replace("open", "uc")
    gdown.download(link, file_path, quiet=False)
    # gdown.download(link, output, quiet=False, fuzzy=True)
    return file_path


def scan_file(file_path: str):
    phone_number = []

    phone_pattern = re.compile(r"(\d{3})[.-/s](\d{3})[.-/s](\d{4})")
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            matches = re.findall(phone_pattern, text)
            if matches:
                phone_number.extend(matches)

    print(phone_number)


if __name__ == '__main__':
    scan_phone_number()

from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url):
    parsed_url = urlsplit(url)
    return parsed_url.netloc + parsed_url.path


def get_heading_from_html(html):
    pass


def get_first_paragraph_from_html(html):
    pass
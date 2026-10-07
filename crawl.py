from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url):
    parsed_url = urlsplit(url)
    return parsed_url.netloc + parsed_url.path


def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    h1_tag = soup.find('h1')
    h2_tag = soup.find('h2')
    if h1_tag and isinstance(h1_tag, Tag):
        return h1_tag.get_text(strip=True)
    elif h2_tag and isinstance(h2_tag, Tag):
        return h2_tag.get_text(strip=True)
    else:
        return ""




def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    main_tag = soup.find('main')
    if main_tag and isinstance(main_tag, Tag):
        p_tag = main_tag.find('p')
        if p_tag and isinstance(p_tag, Tag):
            return p_tag.get_text(strip=True)
    return ""
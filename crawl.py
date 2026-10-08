from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

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


def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    extracted_links = []
    anchors = soup.find_all('a')
    links = [tag.get('href') for tag in anchors if tag.get('href')]
    for link in links:
        final_link = urljoin(base_url, link)
        extracted_links.append(final_link)
    return extracted_links

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    extracted_images = []
    img_tags = soup.find_all('img')
    img_srcs = [tag.get('src') for tag in img_tags if tag.get('src')]
    for src in img_srcs:
        final_src = urljoin(base_url, src)
        extracted_images.append(final_src)
    return extracted_images
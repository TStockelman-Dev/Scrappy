import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    else:
        print(f"starting crawl of: {sys.argv[1]}")
        html = get_html(sys.argv[1])
        print(html)


def get_html(url):
    response = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
    try:
        if response.status_code > 400:
            raise Exception(f"Failed to fetch HTML from {url}, status code: {response.status_code}")
        if response.headers.get("Content-Type") != "text/html":
            raise Exception(f"Expected HTML content from {url}, but got {response.headers.get('Content-Type')}")
        return response.text
    except Exception as e:
        print(e)
        sys.exit(1)

def crawl_page(base_url, current_url = None, page_data = None):
    pass

if __name__ == "__main__":
    main()

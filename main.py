import sys

from crawl import crawl_page


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    print(f"starting crawl of: {base_url}...")

    page_data = crawl_page(base_url)

    print(f"Found {len(page_data)} pages:")
    for page in page_data.values():
        print(f"- {page['url']}: {len(page['outgoing_links'])} outgoing links")

    sys.exit(0)


if __name__ == "__main__":
    main()

import unittest
from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html, get_urls_from_html, get_images_from_html

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "http://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_basic(self):
        input_body = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_heading_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)


    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = """<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>"""
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def get_urls_from_html(self):
        input_body = """<html><body>
            <a href="http://www.boot.dev/blog/path1">Link 1</a>
            <a href="http://www.boot.dev/blog/path2">Link 2</a>
            </body></html>"""
        actual = get_urls_from_html(input_body)
        expected = ["http://www.boot.dev/blog/path1", "http://www.boot.dev/blog/path2"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_relative(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_second(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/second.png" alt="Second"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/second.png"]
        self.assertEqual(actual, expected)

    def test_get_images_from_html_third(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/third.png" alt="Third"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/third.png"]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
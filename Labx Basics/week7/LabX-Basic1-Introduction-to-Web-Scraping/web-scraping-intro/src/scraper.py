# web-scraping-intro/src/scraper.py
import requests
from bs4 import BeautifulSoup

class SimpleWebScraper:
    """
    A class to encapsulate basic web scraping functionality.
    """
    def __init__(self, target_url):
        self.target_url = target_url

    def _get_html_content(self):
        """
        Downloads the HTML content from the target URL.
        Handles basic error checking.
        """
        print(f"กำลังดาวน์โหลด เนื้อหาจาก: {self.target_url}")
        try:
            # Add a User-Agent header to mimic a real browser, as some sites block default requests
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(self.target_url, headers=headers, timeout=10)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            print("ดาวน์โหลด เนื้อหาสำเร็จ")
            return response.text
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e} - Status Code: {e.response.status_code}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e} - Could not connect to {self.target_url}")
            return None
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An unexpected request error occurred: {e}")
            return None

    def scrape_main_titles(self):
        """
        Scrapes the main book title and chapter titles from the Automate the Boring Stuff homepage.
        """
        html_content = self._get_html_content()
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the main book title from the <article><header> section
        article_tag = soup.find('article')
        book_title = "Book Title Not Found"
        if article_tag:
            header_tag = article_tag.find('header')
            if header_tag:
                h1_tag = header_tag.find('h1')
                if h1_tag:
                    book_title = h1_tag.get_text(strip=True)

        # Extract chapter titles from the "Table of Contents" list
        chapter_titles = []
        for link in soup.select('div.content-body ul li a'):
            title = link.get_text(strip=True)
            if title:
                chapter_titles.append(title)

        return {
            "book_title": book_title,
            "chapter_titles": chapter_titles
        }

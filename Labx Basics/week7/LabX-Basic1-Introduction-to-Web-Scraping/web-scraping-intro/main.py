# web-scraping-intro/main.py
import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scraper import SimpleWebScraper

def main():
    """
    Main entry point for the simple web scraping application.
    """
    target_url = "https://automatetheboringstuff.com/3e/"
    scraper = SimpleWebScraper(target_url)

    scraped_data = scraper.scrape_main_titles()

    if scraped_data:
        print("\n--- ข้อมูลที่ Scrape ได้ ---")
        print(f"ชื่อหนังสือ: {scraped_data['book_title']}")
        print("\nบทต่างๆ:")
        if scraped_data['chapter_titles']:
            for i, title in enumerate(scraped_data['chapter_titles']):
                print(f"{i+1}. {title}")
        else:
            print("No chapter titles found.")
        print("--------------------")
    else:
        print("Failed to scrape data.")

if __name__ == "__main__":
    main()

from playwright.sync_api import sync_playwright

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

def fetch_chapter():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        page.screenshot(path="screenshots/chapter1.png", full_page=True)
        content = page.locator("#mw-content-text").inner_text()
        with open("outputs/raw_chapter.txt", "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
        return content

if __name__ == "__main__":
    print("Scraped content:\n", fetch_chapter())

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # 네이버 랭킹 뉴스 진입
    page.goto("https://news.naver.com/main/ranking/popularDay.naver")

    company_title = get_text

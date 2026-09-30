from playwright.sync_api import sync_playwright

#chromium->launch cricbuzz- live match score->take screenshot of the page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Launches a Chromium browser in non-headless mode
    page = browser.new_page()  # Opens a new page in the browser
    page.goto("https://www.cricbuzz.com/")  # Navigates to the Cricbuzz website
    page.click("text=Live Scores")  # Clicks on the "Live Scores" link to view live match scores
    page.click("text=Matches")  # Clicks on the "Matches" text on the page
    #page.click("text=Teams")  # Clicks on the "Live" text to view live matches
    #page.click("text=Matches")  # Clicks on the "Live" text to view live matches
    page.click("text=Matches By Day")  # Clicks on the "Live" text to view live matches
    page.screenshot(path="cricbuzz_live_score.png")  # Takes a screenshot of the page and saves it as 'cricbuzz_live_score.png'
    browser.close()  # Closes the browser
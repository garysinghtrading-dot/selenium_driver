from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setDriver(pathToProfile, u_a):
    chrome_options = Options()

    # Tell Selenium where Chromium lives on GitHub Actions
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={u_a}")

    return webdriver.Chrome(options=chrome_options)

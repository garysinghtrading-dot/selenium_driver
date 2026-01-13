from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setDriver(pathToProfile, u_a):
    chrome_options = Options()

    # Use Snap Chromium
    chrome_options.binary_location = "/snap/bin/chromium"

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={u_a}")

    return webdriver.Chrome(options=chrome_options)

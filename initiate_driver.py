from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setDriver(pathToProfile, u_a):
    #chrome options
    custom_user_profile = "" # path to custom user profile 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent="+u_a)
    # chrome_options.add_argument("user-agent="+u_a) -- custom user profile 
    #chrome_options.add_arguments("") # for custom headers
    # set up chrome driver
    service = Service(get_driver_location())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver 
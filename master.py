# imports
import anchor_tags
import initiate_driver
import user_agents
import drive_driver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import shutil

# remove user profile
def remove_user_profile(path):
    directory_path = path
    try:
        shutil.rmtree(directory_path)
    except:
        print("Could not close directory")

# Get all user agents
nUAclassObject = user_agents.GetUserAgentsCsv()
all_user_agents = nUAclassObject.get_all_user_agents() # getting all user agents

# new object of GetAnchorTagUrl class
newAObject = anchor_tags.GetAnchorTagUrl() # object created

# customer user profile path
user_profile_path = ""

for ua in range(117, len(all_user_agents)):
    urlNavTo = newAObject.get_starting_url() # url to get
    driver = initiate_driver.setDriver(user_profile_path, all_user_agents[ua])
    try:
        drive_driver.driver_driver(driver=driver, url=urlNavTo)
        print(ua, "done")
    except TimeoutException as e:
        print("Timeout exception occured")
        ua -= 1
    try:
        driver.quit()
    except:
        print("driver already quitted")
    #remove_user_profile(user_profile_path) # remove user profile data

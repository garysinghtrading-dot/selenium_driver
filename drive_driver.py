# selenium imports
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
import sys
import time

def genRandNum(a, b):
    number = random.randint(a, b)
    return number

# Class to get new URL to navigate to
class GetNewUrl:
    '''
      Method to check if the url has adsense keywords
      Helper function to checkUrl method
      args:
        url to the webpage to check for adsense keywords
        returns:
        True if the url has adsense keywords, False otherwise
    '''
    def checkAdsenseKeywords(self, url):
      adsense_keywords = {"adclick", "doubleclick", "net", "googleads"}
      for keyword in adsense_keywords:
        if keyword in url:
          return True
      return False

    def checkUrl(self, url_to_evaluate):
        my_domain = "www.accountplusfinance.com" # domain name to evaluate
        href = url_to_evaluate.get_attribute("href") # get href
        if my_domain in href and not self.checkAdsenseKeywords(href):
            return True # the url has the domain in it, return True

        return False # Domain name was not found in the URL

    def getUrl(self, driver):
        all_a_tags = driver.find_elements(By.TAG_NAME, 'a')  # get all anchor tags
        new_url = None
        found = False
        a_tag_counter = 0
        while not found and a_tag_counter < 10:
            rand_atag_num = genRandNum(0, len(all_a_tags)-1)  # random number
            a_tag = all_a_tags[rand_atag_num]
            href = a_tag.get_attribute("href")
            if href:  # Check if href is not empty
                found = self.checkUrl(a_tag)
                if found:
                    new_url = all_a_tags[rand_atag_num]
                    break
            a_tag_counter += 1
        if new_url == None:
            print("no new url found")
            driver.quit()
            return None
        return new_url


# Class to drive the driver
class DriveDriver:
    def setInitialBodyClick(self, driver):
        '''
            method to click the body element
                args:
                    selenium web driver is passed into this function
                clicks the body element soon as the webpage loads
        '''
        driver.execute_script("""
            document.getElementsByTagName('body')[0].click();
        """) # click on body element
        time.sleep(3) # sleep for 3 seconds

    def waitForPage(self, driver, mode):
        '''
            method to wait for webpage to load, waits up to 30 seconds
            args:
                selenium webdriver
        '''
        try:
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))) # wait up to 30 seconds for body to load
            if mode == "initial":
                print("Body element loaded within 30 seconds on initial try")
            else:
                print("Body element loaded within 30 seconds on link click try")
            # element_text = element.text
        except:
            print("waited 30 seconds, timeout occured")
            driver.quit()

    def getClientScreenSize(driver):
        """
        Method to get the client area size (excluding browser UI elements) using Selenium and JavaScript.
        Args:
            driver: Selenium web driver
        Returns:
            Tuple (width, height) representing the client area size
        """
        getScreenSizescript = """
            function getClientScreenSize() {
                const html = document.querySelector('html');
                const width = html.clientWidth;
                const height = html.clientHeight;
                return [width, height];
            }
            return getClientScreenSize();
        """
        client_screen = driver.execute_script(getScreenSizescript)
        return client_screen

    def getRandElement(self, driver):
        all_divs = driver.find_elements(By.TAG_NAME, "div") # all divs on the page
        if len(all_divs) == 0:
            print("error getting divs")
            sys.exit(1)
        rand_div_num = random.randint(0, len(all_divs)-1)
        chosen_element = all_divs[rand_div_num]
        return chosen_element

    def getElementCoordinates(self, driver, sel_element):
        """
        Method to get the coordinates (position) of a specific element using Selenium and JavaScript.
        Args:
            driver: Selenium web driver
            sel_element: WebElement representing the target element
        Returns:
            Tuple (x_left, x_right, y_top, y_bottom) representing the element's position
        """
        script = """
            function getCoordinates(element) {
                const rect = element.getBoundingClientRect();
                const x_left = rect.left;
                const x_right = rect.right;
                const y_top = rect.top;
                const y_bottom = rect.bottom;
                return [x_left, x_right, y_top, y_bottom];
            }
            return getCoordinates(arguments[0]);
        """
        coordinates = driver.execute_script(script, sel_element)
        return coordinates

    def getXandY(self, driver, page_elem):
        x1, x2, y1, y2 = [float(val) for val in self.getElementCoordinates(driver, page_elem)] # get page elements
        xCOr = round(random.uniform(x1, x2), 4) # Get random x coordinates
        yCOr = round(random.uniform(y1, y2), 4) # get a random y coordinates
        return xCOr, yCOr # return coordinates

    def scrollIntoView(self, driver, x, y):
        scroll_intoViewScript = """
            function scrollTo(x,y){
	            window.scrollTo(x,y);
            }
            scrollTo(arguments[0], arguments[1]);
        """
        driver.execute_script(scroll_intoViewScript, x, y)

    def newPageOrNO(self):
        ''''
            Method to determine if we should visit a new page or not
        '''
        newPageInt = random.randint(0, 2)
        if newPageInt == 0:
            return False # Don't go to a new page
        return True

# ^^^^^ end class DriveDriver ^^^^^

def driver_driver(driver, url):
    driver_d = DriveDriver()
    getNewPage = GetNewUrl()

    driver.get(url)
    driver_d.waitForPage(driver, "initial") # wait for page to load

    max_pages_to_visit = 5
    pages_visited = 0

    while pages_visited < max_pages_to_visit:
        try:
            driver_d.setInitialBodyClick(driver) # initial body click
            num_scroll = genRandNum(2, 8) # how many times to scroll
            for _ in range(num_scroll):
                chosen_elem = driver_d.getRandElement(driver) # get the specific element
                xCor, yCor = driver_d.getXandY(driver, chosen_elem)
                driver_d.scrollIntoView(driver, xCor, yCor)# scroll to that element
                time.sleep(genRandNum(5, 10)) # sleep for randomly generated number of seconds

            # No new page has been visited
            if pages_visited == 0:
                new_url_to_visit_1 = getNewPage.getUrl(driver) # new url
                if new_url_to_visit_1 == None:
                    driver.quit()
                    print("had to quit driver because no new url was found")
                    return
                x_url_cor, y_url_cor = driver_d.getXandY(driver, new_url_to_visit_1)
                driver_d.scrollIntoView(driver, x_url_cor, y_url_cor) # scroll to that element # Get url into focus
                time.sleep(2)
                driver.execute_script("arguments[0].click();", new_url_to_visit_1) # click the next url
                driver_d.waitForPage(driver, "not initial") # wait for body element to be loaded on page

            # new page has been visited, now we decide if we are to visit a new page or not
            else:
                cont_or_not = driver_d.newPageOrNO()
                if cont_or_not:
                    new_url_to_visit_2 = getNewPage.getUrl(driver) # new url
                    if new_url_to_visit_2 == None:
                        driver.quit()
                        print("had to quit driver because no new url was found")
                        return
                    x_url_cor, y_url_cor = driver_d.getXandY(driver, new_url_to_visit_2)
                    driver_d.scrollIntoView(driver, x_url_cor, y_url_cor) # scroll to that element # Get url into focus
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", new_url_to_visit_2) # click the next url
                    driver_d.waitForPage(driver, "not initial") # wait for body element to be loaded on page
                else:
                    driver.quit()
                    break

        except (TimeoutException, WebDriverException) as e:
            print("sometype of timeout or webdriver exception occured")
            driver.quit()
            return

        pages_visited += 1
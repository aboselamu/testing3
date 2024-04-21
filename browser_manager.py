from RPA.Browser.Selenium import Selenium 
import logging
from robocorp.tasks import task
logging.basicConfig(level=logging.INFO)


#oppening the site aljazeera.com
browser =None
@task
def opening_the_news_Site():
    global browser
    logging.info("Oppening the browser")
    url ="https://www.aljazeera.com/"
    # logger.info("Opening the news site.")
    browser = Selenium(auto_close = False)
    
    # Define Chrome options to disable popup blocking
    options = [
        "--disable-popup-blocking",
        "--ignore-certificate-errors"
    ]

    

    # Open browser with specified options
    browser.open_available_browser(url, 
                                        browser_selection="Chrome", 
                                        options=options
                                  )
    logging.info("Browser oppened")
@task
def search_the_phrase():
    logging.info("Inside search phrase")
    global browser
    phrase = "Business"
    if(browser):
        logging.info("browser found")
    else:
        logging.info("No browser found")
    # logger.info(f"Searching the phrase: {phrase}")
    # if the site contains collecting cookies 
    try:
        
        browser.click_button('Allow all')
        logging.info("It clicked Allow all")

    except:
        logging.info("it didn't clicked allow")
        pass
    # finding the serach icon and field
    locator1 = "//button[@aria-pressed='false']//*[name()='svg']"
    browser.wait_until_page_contains_element(locator1, timeout=10)
    browser.click_element(locator1)

    # inserting the search phrase in the input field
    browser.input_text("//input[@placeholder='Search']",phrase)
    browser.click_button("//button[@aria-label='Search Al Jazeera']")
    # self.browser.close_all_browsers()


    # Trying to find it there is a realated articles with the search phrase
    try:
        locator2 = "//select[@id='search-sort-option']"
        browser.wait_until_element_is_visible(locator2, timeout=10)
        browser.click_element(locator2)
        logging.info("finding the search area")
    except Exception as e:
        logging.error(f"Can't Find search area: {e}")
    # sort by time
    dropdown_locator = "//select[@id='search-sort-option']/option[1]" 
    browser.click_element(dropdown_locator)
    logging.info("complete Searching")

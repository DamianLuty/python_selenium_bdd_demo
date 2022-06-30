from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# not closing web browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def go_to(url, browser_type=None):
    if not browser_type:
        # create instance of Firefox driver the browser type is not specified
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=chrome_options)
    elif browser_type.lower() == 'chrome':
        # create instance of the Chrome driver
        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    driver.get(url)

    return driver

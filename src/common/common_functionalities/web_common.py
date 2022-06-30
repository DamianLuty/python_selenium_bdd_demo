from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# not closing web browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)


def go_to(url, browser_type=None):
    if not browser_type:
        # create instance of Chrome driver the browser type is not specified
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe", chrome_options=chrome_options)
    elif browser_type == "chrome":
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe", chrome_options=chrome_options)
    elif browser_type == "edge":
        driver = webdriver.Chrome(executable_path="./drivers/msedgedriver.exe")
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to the url
    url = url.strip()
    driver.get(url)

    return driver


def searching_loop(web_element_list, expected_value):
    for element in web_element_list:
        element_text = element.text.lower()
        if expected_value in element_text:
            return element_text
            break
    return "Value was not found"



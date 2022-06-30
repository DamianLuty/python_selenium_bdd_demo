from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.python_search_page import SearchPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    _python_logo = (By.CSS_SELECTOR, "img[class='python-logo']")
    _navigation_menu_about_button = (By.ID, "about")
    _navigation_menu_about_downloads = (By.ID, "downloads")
    _navigation_menu_about_documentation = (By.ID, "documentation")
    _navigation_menu_about_community = (By.ID, "community")
    _navigation_menu_about_success_stories = (By.ID, "success-stories")
    _search_field = (By.CSS_SELECTOR, "input[class='search-field']")
    _search_go_button = (By.ID, "submit")

    def get_url(self):
        return self.driver.current_url

    def get_python_logo_text(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._python_logo))
        return self.driver.find_element(*self._python_logo).get_attribute('alt')

    def set_searching_input(self, input_phrase):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._search_field))
        search_field = self.driver.find_element(*self._search_field)
        search_field.clear()
        search_field.send_keys(input_phrase)

    def get_searching_input(self):
        return self.driver.find_element(*self._search_field).get_attribute('value')

    def search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self._python_logo))
        self.driver.find_element(*self._search_go_button).click()
        search_page = SearchPage(self.driver)
        return search_page


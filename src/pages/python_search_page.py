from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    _search_section_text = (By.TAG_NAME, "h2")
    _search_results = (By.CSS_SELECTOR, "ul[class='list-recent-events menu'] h3")

    def section_text_check(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self._search_section_text))
        expected_text = "Search Python.org"
        section_text = self.driver.find_element(*self._search_section_text).text()
        assert section_text == expected_text, f"Text not found, shoudl be: {expected_text}, instead of: {section_text}"

    def get_searched_result_titles(self):

        return self.driver.find_elements(*self._search_results)

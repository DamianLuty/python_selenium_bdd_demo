from seleniumpagefactory.Pagefactory import PageFactory


class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

        locators = {
            'page_logo' : ('CSS', "img[class='python-logo']")
        }
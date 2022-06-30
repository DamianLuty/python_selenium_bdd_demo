from behave import *

from src.common.common_configs import urls
from src.common.common_functionalities import web_common
from src.pages.python_main_page import MainPage
from src.pages.python_search_page import SearchPage


@given('User enters to a "{website}" main page')
def getting_url(context, website):
    context.url_in_test = urls.URLCONFIG.get(website)
    context.driver = web_common.go_to(context.url_in_test)


@when('User enter a "{phrase}" text in search field')
def searching_by_phrase(context, phrase):
    context.phrase = phrase
    python_main_page = MainPage(context.driver)
    python_main_page.set_searching_input(phrase)
    python_main_page.search_button()


@Then('the main page should be displayed')
def checking_main_page(context):
    python_main_page = MainPage(context.driver)

    current_url = python_main_page.get_url()
    assert current_url == context.url_in_test, f"Incorrect url, current url: {current_url}, " \
                                               f"while tested is: {context.url_in_test}"

    expected_logo = "python™"
    logo_text = python_main_page.get_python_logo_text()
    assert expected_logo == logo_text, f"Logo not found, should be: {expected_logo} , but is: {logo_text}"


@Then('The search results should be displayed')
def checking_search_results(context):
    python_main_page = MainPage(context.driver)
    python_search_page = SearchPage(context.driver)
    text_from_search_field_after_input = python_main_page.get_searching_input()
    assert text_from_search_field_after_input == context.phrase, f"Text in the search field is incorrect than in the " \
                                                                 f"step definition, should be: {context.phrase}, " \
                                                                 f"but is: {text_from_search_field_after_input}"
    # checking does the the results contain searched item
    searched_result = web_common.searching_loop(python_search_page.get_searched_result_titles(), context.phrase.lower())
    assert context.phrase.lower() in searched_result, f"{searched_result}, {context.phrase.lower()}"


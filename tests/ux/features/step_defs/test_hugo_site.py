"""Hugo Site Test Suite"""
from pytest_bdd import scenario, given, when, then  # noqa: E501 # pylint: disable=import-error
from selenium.webdriver.support.ui import (WebDriverWait)  # noqa: E501 # pylint: disable=import-error
from selenium.webdriver.common.by import (By)  # noqa: E501 # pylint: disable=import-error
from selenium.webdriver.support import (expected_conditions as EC)  # noqa: E501 # pylint: disable=import-error

DEFAULT_TIMEOUT = 15


def get_default_url(url):
    "gets the default url of the site and appends / to it if necessary"
    if url[-1] == "/":
        return url
    return url + "/"


def get_button_link_by_name(browser, linktext):
    "will click on a button when given the name of the link to press"
    return browser.find_elements(By.LINK_TEXT, linktext)


@scenario('../hugo_tests.feature', 'Test index page')
def test_index_page_result():
    """Test index page."""


@scenario('../hugo_tests.feature', 'Test first page')
def test_first_page_result():
    """Test first page."""


@scenario('../hugo_tests.feature', 'Test second page')
def test_second_page_result():
    """Test second page."""


@given('you launch Chrome Browser and you have your site running')
def wait_page_load(browser, url, get_default_title):
    """Loads the page"""
    browser.get(url)
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(EC.title_is(get_default_title))  # noqa: E501


@when('you open the page')
def load_index_page(browser, url, get_default_title):
    """Basically repeats step before"""
    wait_page_load(browser, url, get_default_title)


@then('verify your chrome browser is at the correct url and the title of the page is Hugo Site')  # noqa: E501  # pylint: disable=line-too-long
def index_page(browser, url, get_default_title):
    """check the index page is configured correctly"""
    page_url = get_default_url(url)
    page_title = get_default_title
    load_index_page(browser, url, get_default_title)
    assert page_title == browser.title
    assert page_url == browser.current_url


@then('take a screenshot of the index page')
def scrnshot_index(browser):
    """Screenshot of index page taken"""
    browser.save_screenshot("test_index_page_00.png")


@given('you move to testing the first page')
def load_page_1(browser, url, get_default_title):
    """Loads the first page"""
    load_index_page(browser, url, get_default_title)
    page_url = get_default_url(url)+"posts/baqir/"
    page_title = "Baqir | " + get_default_title

    wait_page_load(browser, page_url, page_title)


@when('you verify you are at the correct page url and the title is Baqir | Hugo Site')  # noqa: E501
def step_impl(browser, url, get_default_title):
    """Tests for the url and title of first page"""
    page_url = get_default_url(url)+"posts/baqir/"
    page_title = "Baqir | " + get_default_title
    assert page_url == browser.current_url
    assert page_title == browser.title


@then('check the text of the page on baqir is the same as your assertion')
def text_page_1(browser):
    """tests the text of the page"""
    text = "Baqir, 24, formerly a cloud engineer, informally a Man United fan."  # noqa: E501 # pylint: disable=line-too-long
    text_site = browser.find_element(By.XPATH, "/html/body/main/article/div/p[1]").text  # noqa: E501 # pylint: disable=line-too-long
    assert text_site == text


@then('verify the images on your page exist, testing')
def image_page_1(browser, url):
    """tests the images on page 1"""
    example_images = browser.find_elements(By.TAG_NAME, 'img')
    if example_images:
        for image in example_images:
            current_link = image.get_attribute("src")
            current_title = image.get_attribute("title")
            current_alt = image.get_attribute("alt")

            if current_alt == "Teams":
                assert current_link == get_default_url(url)+"images/teams.png"  # noqa: E501
                assert current_title == "Baqir"

            elif current_alt == "Baqir":
                assert current_link == get_default_url(url)+"images/baqir.png"  # noqa: E501
                assert current_title == "Baqir"


@then('take a screenshot of the first page')
def scrnshot_first_page(browser):
    """screenshot of first page taken"""
    browser.save_screenshot("test_first_page_00.png")


@given('you move to testing the second page')
def load_page_2(browser, url, get_default_title):
    """Loads the second page"""
    load_index_page(browser, url, get_default_title)

    page_url = get_default_url(url)+"posts/iphone/"
    page_title = "iphone | " + get_default_title

    wait_page_load(browser, page_url, page_title)


@when('you verify you are at the correct page url and the title is iphone | Hugo Site')  # noqa: E501 # pylint: disable=line-too-long
def url_title_page_2(browser, url, get_default_title):
    """tests url and title of second page"""
    page_url = get_default_url(url)+"posts/iphone/"
    page_title = "iphone | " + get_default_title
    assert page_url == browser.current_url
    assert page_title == browser.title


@then('check the text of the page is the same as the poem on the page')
def text_page(browser):
    """tests text of the second page"""
    text = "I got ChatGPT to make a disstrack on Android from iphone:\nYou may have some customization, but it’s just a distraction,\nWe offer a seamless experience, without any fraction,\nOur design is iconic, it’s sleek and refined,\nAndroid, you’re just a copycat, always a step behind."  # pylint: disable= line-too-long  # noqa: E501
    text_page_2 = browser.find_element(By.XPATH, "/html/body/main/article/div").text  # noqa: E501
    assert text_page_2 == text


@then('verify there are no images this page')
def image_checker(browser):
    """tests if images are in the second page"""
    example_images = browser.find_elements(By.TAG_NAME, 'img')
    if example_images:
        raise AssertionError


@then('take a screenshot of the second page')
def scrnshot_second_page(browser):
    """takes screenshot of page"""
    browser.save_screenshot("test_second_page_00.png")

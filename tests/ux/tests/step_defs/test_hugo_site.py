from pytest_bdd import scenario, given, when, then
import pytest
from selenium.webdriver.support.ui import (WebDriverWait)
from selenium.webdriver.common.by import (By)
from selenium.webdriver.support import (expected_conditions as EC)
from behave import *

DEFAULT_TIMEOUT = 15
SITENAME = "Hugo Site"


def get_default_url(url):
    "gets the default url of the site and appends / to it if necessary"
    url = "http://localhost:1313/"
    if url[-1] == "/":
        return url
    return url + "/"


def get_default_title():
    "returns the sitename specified as a constant var SITENAME"
    return SITENAME

@pytest.mark.usefixtures("driver_init")
class TestHugo():

    def get_button_link_by_name(self, linktext):
        "will click on a button when given the name of the link to press"
        return self.driver.find_elements(By.LINK_TEXT, linktext)

    
    # @scenario('../hugo_tests.feature', 'Test index page')
    def test_publish():
        pass

    @given(u'you launch Chrome Browser and you have your site running')
    def wait_page_load(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.title_is(self.driver.title))  # noqa: E501


    @when(u'you open the page')
    def load_index_page(self, url):
        self.wait_page_load(url, get_default_title())


    @then(u'verify your chrome browser is at the correct url and the title of the page is Hugo Site')
    def test_index_page(self, url):
        """check the index page is configured correctly"""
        page_url = get_default_url(url)
        page_title = get_default_title()
        self.load_index_page(url)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
    

    @then(u'take a screenshot of the index page')
    def scrnshot_index(self):
        self.driver.save_screenshot("test_index_page_00.png")

    # @scenario('../hugo_tests.feature', 'Test first page')
    @given(u'you move to testing the first page')
    def load_page_1(context, self, url):
        self.load_index_page(url)
        context.page_url = get_default_url(url)+"posts/baqir/"
        context.page_title = "Baqir | " + get_default_title()

        self.wait_page_load(context.page_url, context.page_title)


    @when(u'you verify you are at the correct page url and the title is Baqir | Hugo Site')
    def step_impl(context, self):
        assert context.page_url == self.driver.current_url
        assert context.page_title == self.driver.title


    @then(u'check the text of the page on baqir is the same as your assertion')
    def text_page_1(self):
        text = "Baqir, 24, formerly a cloud engineer, informally a Man United fan."  # noqa: E501
        text_site = self.driver.find_element(By.XPATH, "/html/body/main/article/div/p[1]").text  # noqa: E501
        assert text_site == text

    @then(u'verify the images on your page exist, testing')
    def image_page_1(self, url):
        example_images = self.driver.find_elements(By.TAG_NAME, 'img')
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
    @then(u'take a screenshot of the first page')
    def scrnshot_first_page(self):
        self.driver.save_screenshot("test_first_page_00.png")
    
    # @scenario('../hugo_tests.feature', 'Test second page')
    @given(u'you move to testing the second page')
    def load_page_2(context, self, url):
        self.load_index_page(url)

        context.page_url = get_default_url(url)+"posts/iphone/"
        context.page_title = "iphone | " + get_default_title()

        self.wait_page_load(context.page_url, context.page_title)

    @when(u'you verify you are at the correct page url and the title is iphone | Hugo Site')
    def url_title_page_2(context, self):
        assert context.page_url == self.driver.current_url
        assert context.page_title == self.driver.title


    @then(u'check the text of the page is the same as the poem on the page')
    def text_page_2(context, self):
        text = "I got ChatGPT to make a disstrack on Android from iphone:\nYou may have some customization, but it’s just a distraction,\nWe offer a seamless experience, without any fraction,\nOur design is iconic, it’s sleek and refined,\nAndroid, you’re just a copycat, always a step behind."  # pylint: disable= line-too-long  # noqa: E501
        text_page_2 = self.driver.find_elements(By.XPATH, "/html/body/main/article/div")  # noqa: E501
        assert text_page_2 == text


    @then(u'verify there are no images this page')
    def image_checker(context, self):
        example_images = self.driver.find_elements(By.TAG_NAME, 'img')
        if example_images:
            raise AssertionError
        else:
            pass
    
    
    @then(u'take a screenshot of the second page')
    def scrnshot_second_page(self):
        self.driver.save_screenshot("test_second_page_00.png")

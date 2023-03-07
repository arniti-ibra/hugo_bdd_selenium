"""Hugo Test Suite"""

# pylint: disable=no-member
# pylint: disable=line-too-long
# pylint: disable=import-error
import pytest
from selenium.webdriver.support.ui import (
    WebDriverWait
    )
from selenium.webdriver.common.by import (
    By
    )
from selenium.webdriver.support import (
    expected_conditions as EC
    )


DEFAULT_TIMEOUT = 15
SITENAME = "Hugo Site"


def get_default_url(url):
    "gets the default url of the site and appends / to it if necessary"
    if url[-1] == "/":
        return url
    return url + "/"


def get_default_title():
    "returns the sitename specified as a constant var SITENAME"
    return SITENAME


@pytest.mark.usefixtures("driver_init")
class TestHugo:
    "The Test Class itself, uses the fixture setup from the conftest file."
    def get_button_link_by_name(self, linktext):
        "will click on a button when given the name of the link to press"
        return self.driver.find_elements(By.LINK_TEXT, linktext)

    def wait_page_load(self, url, title):  # pylint: disable=unused-argument
        # noqa: E501
        """# noqa: E501
        When a page is loaded by the browser,
        the elements within that page may load at different time intervals. Waits can solve this issue.
        This example is an explicit wait until a condition is statisfied. Had to import EC to enable this.
        It waits for a maximum of 15 seconds, the condition is that the title matches what the webdriver scrapes"""
        self.driver.get(url)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.title_is(self.driver.title))  # noqa: E501

    def load_index_page(self, url):
        """Load the index page"""
        self.wait_page_load(url, get_default_title())

    def test_index_page(self, url):
        """check the index page is configured correctly"""
        page_url = get_default_url(url)
        page_title = get_default_title()

        self.load_index_page(url)
        assert page_title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_index_page_00.png")

    def test_first_page(self, url):
        """# noqa: E501
        check the first page for its title, url and tests the 2 images images present as well as their dimensions match what you would expect"""

        self.load_index_page(url)
        page_url = get_default_url(url)+"posts/baqir/"
        page_title = "Baqir | " + get_default_title()

        self.wait_page_load(page_url, page_title)
        assert page_url == self.driver.current_url
        assert page_title == self.driver.title

        text = "Baqir, 24, formerly a cloud engineer, informally a Man United fan."  # noqa: E501
        for content in self.driver.find_elements(By.XPATH, "/html/body/main/article/div/p[1]"):  # noqa: E501
            assert content.text == text

        example_images = self.driver.find_elements(By.TAG_NAME, 'img')
        if example_images:
            for image in example_images:
                current_link = image.get_attribute("src")
                current_title = image.get_attribute("title")
                current_alt = image.get_attribute("alt")

                if current_alt == "Teams":
                    # dimensions = image.size
                    assert current_link == get_default_url(url)+"images/teams.png"  # noqa: E501
                    assert current_title == "Baqir"
                    # try:
                    #     assert dimensions == {'height': 333, 'width': 629}

                    # finally:
                    #     print(f"{AssertionError}\nThe dimensions for the the image with link {current_link} do not match what is asserted")  # noqa: E501
                elif current_alt == "Baqir":
                    # dimensions = image.size
                    assert current_link == get_default_url(url)+"images/baqir.png"  # noqa: E501
                    assert current_title == "Baqir"
                    # try:
                    #     assert dimensions == {'height': 472, 'width': 542}

                    # finally:
                    #     print(f"{AssertionError}\nThe dimensions for the the image with link {current_link} do not match what is asserted")  # noqa: E501

        self.driver.save_screenshot("test_first_page_00.png")

    def test_second_page(self, url):
        """Tests second page for title, url and images only if it has them"""
        self.load_index_page(url)

        page_url = get_default_url(url)+"posts/iphone/"
        page_title = "iphone | " + get_default_title()

        self.wait_page_load(page_url, page_title)

        assert page_url == self.driver.current_url
        assert page_title == self.driver.title

        text = "I got ChatGPT to make a disstrack on Android from iphone:\nYou may have some customization, but it’s just a distraction,\nWe offer a seamless experience, without any fraction,\nOur design is iconic, it’s sleek and refined,\nAndroid, you’re just a copycat, always a step behind."  # pylint: disable= line-too-long  # noqa: E501
        for content in self.driver.find_elements(By.XPATH, "/html/body/main/article/div"):  # noqa: E501
            assert content.text == text

        example_images = self.driver.find_elements(By.TAG_NAME, 'img')
        if example_images:
            for image in example_images:
                current_link = image.get_attribute("src")
                current_title = image.get_attribute("title")
                current_alt = image.get_attribute("alt")

                if current_alt == "Teams":
                    dimensions = image.size
                    assert current_link == get_default_url(url)+"images/teams.png"  # noqa: E501
                    assert current_title == "Baqir"
                    try:
                        assert dimensions == {'height': 333, 'width': 629}

                    finally:
                        print(f"{AssertionError}\nThe dimensions for the the image with link {current_link} do not match what is asserted")  # noqa: E501
        self.driver.save_screenshot("test_second_page_00.png")

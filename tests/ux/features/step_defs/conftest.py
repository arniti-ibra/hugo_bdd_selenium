"""Allow configuration for python and selenium parameters"""

import pytest
# pylint: disable=line-too-long
# pylint: disable=import-error
from selenium import webdriver
from selenium.webdriver.firefox.options import (
    Options as FirefoxOptions
    )

from selenium.webdriver.chrome.options import (
    Options as ChromeOptions
  )
# pylint: disable=import-error
from selenium.webdriver.edge.options import (
    Options as EdgeOptions
  )
# pylint: disable=import-error


def pytest_addoption(parser):
    """Add options for Selenium"""
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--headless", action="store", default="No")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")
    parser.addoption("--url", action="store")


@pytest.fixture
def username(request):
    """Get the username option"""
    return request.config.getoption("--username")


@pytest.fixture
def password(request):
    """Get the password option"""
    return request.config.getoption("--password")


@pytest.fixture
def url(request):
    """Get the target URL"""
    return request.config.getoption("--url")


SITENAME = "Hugo Site"


@pytest.fixture
def get_default_title():
    "returns the sitename specified as a constant var SITENAME"
    return SITENAME


@pytest.fixture(params=['chrome',
                        'edge',
                        'firefox'], scope="session", autouse=True)
def browser(request):
    """Setup the required browser with the command line options"""
    if request.param == 'edge':
        options = EdgeOptions()
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--log-level=3")
        driver = webdriver.Edge(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        driver = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--hide-scrollbars')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--disable-popup-blocking")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    # Start function
    yield driver

    # Teardown code
    driver.close()
    driver.quit()

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

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

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


@pytest.fixture(params=['chrome', 'edge', 'firefox'], scope="class")
def driver_init(request):
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
# Still need to get unique screenshots for each browser
    driver.implicitly_wait(10)
    request.cls.driver = driver
    # Start function
    yield driver

    # Teardown code
    driver.close()
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrom')  # Switch to 'headless' to non-ui
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920, 1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)  # executable_pass = r'C:\Webdrivers\chromedriver.exe'
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from abstract.selenium_listener import ClickListener

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
    #driver = EventFiringWebDriver(driver, ClickListener()) - Delete cookie that detects that browser is driven by selenium
    if request.cls is not None:
        request.cls.driver = driver
   #driver.delete_all_cookies()
    yield driver
    driver.quit()

import time
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from abstract.selenium_listener import ClickListener


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')  # Switch to 'headless' to non-ui
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920, 1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    install_chromedriver = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=install_chromedriver,
                              options=options)  # #or use executable_pass to chromedriver.exe'
    return driver

@pytest.fixture(scope='function')
def setup_and_teardown(request, get_webdriver):
    global driver
    driver = get_webdriver
    # driver = EventFiringWebDriver(driver, ClickListener()) - Delete cookie that detects that browser is driven by selenium
    if request.cls is not None:
        request.cls.driver = driver
    # driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(report):
    if report.failed:
        screen = driver.get_screenshot_as_png()
        date_time = datetime.now().replace(second=0, microsecond=0)
        allure.attach(screen, name=f"Snapshot_{date_time}", attachment_type=allure.attachment_type.PNG)

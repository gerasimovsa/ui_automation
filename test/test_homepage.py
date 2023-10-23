import pytest
import allure
from pom.homepage import Homepage


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Homepage")
class TestHomepage:
    @allure.feature("Homepage navigation")
    class TestNavigationLinks:
        @allure.title("Navigation links text test")
        def test_nav_links(self):
            homepage = Homepage(self.driver)
            CARDS_AND_URLS = {"Elements": "https://demoqa.com/elements",
                              "Forms": "https://demoqa.com/forms",
                              "Alerts, Frame & Windows": "https://demoqa.com/alertsWindows",
                              "Widgets": "https://demoqa.com/widgets",
                              "Interactions": "https://demoqa.com/interaction",
                              "Book Store Application": "https://demoqa.com/books"}
            homepage.open_page()
            urls = homepage.get_card_urls(CARDS_AND_URLS.keys())
            assert urls == list(CARDS_AND_URLS.values()), "Validating that correct urls are opened from homepage"

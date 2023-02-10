import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_text = homepage_nav.get_nav_links_text()
        expected_text = homepage_nav.NAV_LINKS_TEXT
        assert actual_text == expected_text, 'Validating header navigation links text'

        for indx in range(13):
            homepage_nav.get_nav_links()[indx].click()


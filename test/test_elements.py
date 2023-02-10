import time

import pytest
from pom.elements_page import TextBoxPage


@pytest.mark.usefixtures('setup')
class TestElementsPage:

    def test_elements_page_field(self):
        text_box_page = TextBoxPage(self.driver)
        text_box_page.fill_all_fields()
        time.sleep(5)

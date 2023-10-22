from base.base_page import BasePage


class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_card_urls(self, cards: list[str]) -> list[str]:
        urls = []
        for card in cards:
            link = self.has_text(card)
            self.go_to_element(link)
            link.click()
            url = self.driver.current_url
            urls.append(url)
            self.open_page()
        return urls

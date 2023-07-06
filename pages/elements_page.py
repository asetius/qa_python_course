from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Asset Kussainov')
        self.element_is_visible(self.locators.EMAIL).send_keys('asetius2008@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Astana')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Astana')
        self.element_is_visible(self.locators.SUBMIT).click()

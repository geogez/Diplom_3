import time

from locators.locators import Construction as cp
from pages.base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open_and_close_modal_window_ingredient(self):
        self.click_on_element(cp.first_ingredient)
        self.wait_element(cp.check_text_details_ingredient)
        self.get_element_text(cp.check_text_details_ingredient)
        self.wait_element(cp.close_ingredient_window)
        self.click_on_element(cp.close_ingredient_window)
        self.wait_until_element_invisible(cp.close_ingredient_window)

    def get_first_count_ingredient(self):
        # Возвращаем текст первого ингредиента
        return self.find(cp.first_ingredient).text

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

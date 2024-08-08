import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)

    def click_on_element(self, locator):
        button = self.browser.find_element(*locator)
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator))
        try:
            button.click()
        except ElementClickInterceptedException:
            # Если клик был перехвачен, прокручиваем страницу и пробуем еще раз
            self.browser.execute_script("arguments[0].scrollIntoView();", button)
            button.click()

    def get_element_text(self, locator):
        element_dom = self.browser.find_element(*locator)
        return element_dom.text

    def fill_field(self, locator, value):
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(value)

    def find(self, locator):
        return self.browser.find_element(*locator)

    def wait_element(self, locator):
        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(locator))

    def drag_and_drop_method(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    def wait_until_element_invisible(self, locator):
        WebDriverWait(self.browser, 10).until(ec.invisibility_of_element_located(locator))

    def wait_for_text_disappear(self, locator, text):
        WebDriverWait(self.browser, 20).until_not(ec.text_to_be_present_in_element(locator, text))

    def wait_for_text_appear(self, locator, text):
        WebDriverWait(self.browser, 20).until(ec.text_to_be_present_in_element(locator, text))

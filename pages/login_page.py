from locators.locators import MainPageLocators as mp
from locators.locators import PathRecoveryPages as rp
from data.data import UserData as ud
from pages.base_pages import BasePage

class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def authorize(self):
        self.click_on_element(rp.account_entry)
        self.fill_field(rp.input_email_user, ud.email)
        self.fill_field(rp.input_password_user, ud.password)
        self.click_on_element(rp.button_enter)

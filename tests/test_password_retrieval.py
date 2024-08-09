from locators.locators import MainPageLocators as mp
from pages.login_page import LoginPage
from locators.locators import PathRecoveryPages as rp
import allure

from data_strings import DataStrings


class TestPersonalAccount:
    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_click_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.wait_element(mp.check_text_account_pages)
        assert login_page.get_element_text(
            mp.check_text_account_pages) == DataStrings.you_can_change_your_personal_data

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход в раздел «История заказов»,')
    def test_click_order_history(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.click_on_element(mp.order_history)
        login_page.wait_element(mp.check_text_order_history)
        assert login_page.get_element_text(mp.check_text_order_history) in DataStrings.completed

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('выход из аккаунта.')
    def test_exit_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.click_on_element(mp.exit_button)
        login_page.wait_for_text_appear(rp.recovery_password, DataStrings.recover_password)

from locators.locators import MainPageLocators as mp
from pages.login_page import LoginPage
from locators.locators import PathRecoveryPages as rp
import allure


class TestPersonalAccount:
    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_click_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.wait_element(mp.check_text_account_pages)
        assert login_page.get_element_text(mp.check_text_account_pages) == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход в раздел «История заказов»,')
    def test_click_order_history(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.click_on_element(mp.order_history)
        login_page.wait_element(mp.check_text_order_history)
        assert login_page.get_element_text(mp.check_text_order_history) in "Выполнен"

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('выход из аккаунта.')
    def test_exit_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.account_autorize_button)
        login_page.click_on_element(mp.exit_button)
        login_page.wait_element(rp.check_text_on_page_recovery_password)
        assert login_page.get_element_text(rp.check_text_on_page_recovery_password) == 'Восстановить пароль'

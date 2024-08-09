from locators.locators import PathRecoveryPages as rp
from pages.base_pages import BasePage
from data.data import UserData as ud
import allure

from data_strings import DataStrings


class TestCheckRecoveryPasswordPage:

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_check_recovery_password_page(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.account_entry)
        base_page.click_on_element(rp.recovery_password)
        assert base_page.get_element_text(rp.check_text_on_page_recovery_password) == DataStrings.password_recovery

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_mail_and_click_button_recovery(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.account_entry)
        base_page.click_on_element(rp.recovery_password)
        base_page.fill_field(rp.input_email_user, ud.email)
        base_page.click_on_element(rp.recovery_button)
        assert base_page.get_element_text(rp.check_text_code_recovery_password) == DataStrings.enter_code_from_email

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.account_entry)
        base_page.fill_field(rp.input_password_user, ud.password)
        base_page.click_on_element(rp.eye_button)
        assert base_page.wait_element(rp.check_activ_eye_button) is not None

import time

from pages.order_page import OrderPage
from pages.login_page import LoginPage
from locators.locators import MainPageLocators as mp
from locators.locators import OrderFeed as of
from locators.locators import Construction as cp
import allure

class TestOrderFeed:

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_order_details(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.order_list)
        order_page.click_on_element(of.first_order)
        assert order_page.get_element_text(of.check_text_details_order) == 'Cостав'

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_order_show_page_order_feed(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = order_page.find(cp.bay_burger)
        target = order_page.find(cp.basket)
        order_page.drag_and_drop_method(source, target)
        login_page.click_on_element(cp.click_order)
        order_count = login_page.get_element_text(of.indicator_count_order)
        login_page.click_on_element(mp.account_autorize_button)
        login_page.click_on_element(mp.order_history)
        order_count_in_account = login_page.get_element_text(of.indicator_count_order_in_personal_account)
        assert order_count in order_count_in_account

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_counter_is_increasing_all_time(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.order_list)
        all_time_orders = int(order_page.get_element_text(of.count_all_time))
        order_page.click_on_element(cp.constructor)
        source = order_page.find(cp.first_ingredient)
        target = order_page.find(cp.basket)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.click_order)
        order_page.click_on_element(of.close_modal_wind)
        order_page.click_on_element(mp.order_list)
        all_time_orders_after = int(order_page.get_element_text(of.count_all_time))
        assert all_time_orders < all_time_orders_after

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_counter_is_increasing_today(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.order_list)
        today_orders = int(order_page.get_element_text(of.count_today))
        source = order_page.find(cp.bay_burger)
        target = order_page.find(cp.basket)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.click_order)
        order_page.click_on_element(of.close_modal_wind)
        order_page.click_on_element(mp.order_list)
        today_orders_after = int(order_page.get_element_text(of.count_today))
        assert today_orders < today_orders_after

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_new_order_show_in_list_in_progress(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = order_page.find(cp.bay_burger)
        target = order_page.find(cp.basket)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.click_order)
        number_order = login_page.get_element_text(of.indicator_count_order)
        order_page.click_on_element(of.close_modal_wind)
        order_page.click_on_element(mp.order_list)
        in_progress = order_page.get_element_text(of.order_in_progress)
        assert number_order == in_progress

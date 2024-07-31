import time

from locators.locators import MainPageLocators as mp
from locators.locators import Construction as cp
from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure


class TestMainFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Конструктор»')
    def test_click_construction(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(mp.order_list)
        assert main_page.get_element_text(mp.total_order_count) is not None

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Лента заказов»')
    def test_click_constructions(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(mp.order_list)
        main_page.click_on_element(mp.construction_button)
        assert main_page.get_element_text(mp.check_text_on_construction_page) == 'Соберите бургер'

    @allure.title('Проверка основного функционала')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(cp.first_ingredient)
        assert main_page.get_element_text(cp.check_text_details_ingredient) == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('всплывающее окно закрывается кликом по крестику')
    def test_close_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.open_and_close_modal_window_ingredient()
        assert not main_page.is_element_visible(cp.check_text_details_ingredient), 'Окно не закрылось'

    @allure.title('Проверка основного функционала')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredients(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        count_start = int(main_page.get_element_text(cp.check_ingredient_count))
        source = login_page.find(cp.bay_burger)
        target = login_page.find(cp.basket)
        login_page.drag_and_drop_method(source, target)
        count_finish = int(main_page.get_element_text(cp.check_ingredient_count))
        assert count_start < count_finish

    @allure.title('Проверка основного функционала')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_authorized_order(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find(cp.bay_burger)
        target = login_page.find(cp.basket)
        login_page.drag_and_drop_method(source, target)
        login_page.click_on_element(cp.click_order)
        assert main_page.get_element_text(cp.check_text_successful_order) == 'Ваш заказ начали готовить'


from selenium.webdriver.common.by import By


class PathRecoveryPages:
    account_entry = (By.XPATH, "//button[text()='Войти в аккаунт']")
    recovery_password = (By.XPATH, "//*[text()='Восстановить пароль']")
    check_text_on_page_recovery_password = (By.XPATH, "//*[text()='Восстановление пароля']")
    input_email_user = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    recovery_button = (By.XPATH, "//*[text()='Восстановить']")
    check_text_code_recovery_password = (By.XPATH, "//label[text()='Введите код из письма']")
    input_password_user = (By.XPATH, "//input[@name='Пароль']")
    eye_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    check_activ_eye_button = (By.XPATH, ".//*[contains(@class, 'input_status_active')]")
    button_enter = (By.XPATH, './/button[contains(text(),"Войти")]')
    register_button = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')


class MainPageLocators:
    account_autorize_button = (By.XPATH, "//*[contains(text(),'Личный Кабинет')]")
    check_text_account_pages = (By.XPATH, '//*[contains(text(),"персональные данные")]')
    order_history = (By.XPATH, "//*[text()='История заказов']")
    check_text_order_history = (By.XPATH, '//p[contains(text(), "Выполнен")]')
    exit_button = (By.XPATH, "//button[text()='Выход']")
    order_list = (By.XPATH, "//*[text() = 'Лента Заказов']")
    total_order_count = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    construction_button = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    check_text_on_construction_page = (By.XPATH, '//*[text()="Соберите бургер"]')


class Construction:
    first_ingredient = (By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]')
    check_text_details_ingredient = (By.XPATH, "//*[contains(text(), 'Детали ингредиента')]")
    close_ingredient_window = (By.XPATH, '//*[contains(@class, "Modal_modal__close")]')
    check_ingredient_count = (By.XPATH, "//*[contains(@class, 'totalContainer')]")
    basket = (By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__list_')]")
    click_order = (By.XPATH, "//*[text()='Оформить заказ']")
    successful_order = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')
    constructor = (By.XPATH, "//*[text()='Конструктор']")


class OrderFeed:
    first_order = (By.XPATH, "(//*[contains(@class, 'OrderHistory_dataBox')])[1]")
    check_text_details_order = (By.XPATH, "//*[text()='Cостав']")
    indicator_count_order = (By.XPATH, "//*[contains(@class, 'Modal_modal__title_shadow_')]")
    indicator_count_order_in_personal_account = (By.XPATH, "(//*[contains(@class, 'OrderHistory_textBox')])[last()]")
    count_all_time = (By.XPATH, "(//*[contains(@class, 'OrderFeed_number_')])[1]")
    count_today = (By.XPATH, "(//*[contains(@class, 'OrderFeed_number_')])[2]")
    close_modal_wind = (By.XPATH, "//*[contains(@class, 'modal__close')]")
    order_in_progress = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    order_number_in_progress = (By.XPATH, "//*[text()='В работе:']/following-sibling::*[2]")
    all_orders_completed = (By.XPATH, "//*[text()='Все текущие заказы готовы!']")

from selenium.webdriver.common.by import By

class PathRecoveryPages:
    account_entry = (By.XPATH, "//button[text()='Войти в аккаунт']")
    recovery_password = (By.XPATH, "//*[text()='Восстановить пароль']")
    check_text_on_page_recovery_password = (By.XPATH, "//*[text()='Восстановление пароля']")
    input_email_user = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    recovery_button = (By.XPATH, "//button[text()='Восстановить']")
    check_text_code_recovery_password = (By.XPATH, "//label[text()='Введите код из письма']")
    input_password_user = (By.XPATH, "//input[@name='Пароль']")
    eye_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    check_activ_eye_button = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
    button_enter = (By.XPATH, './/button[contains(text(),"Войти")]')
    register_button = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')

class MainPageLocators:
    account_autorize_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    check_text_account_pages = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]')
    account_user_button = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]')
    order_history = (By.XPATH, "//a[text()='История заказов']")
    check_text_order_history = (By.XPATH, '//p[contains(text(), "Выполнен")]')
    exit_button = (By.XPATH, "//button[text()='Выход']")
    order_list = (By.XPATH, "//p[text() = 'Лента Заказов']")
    total_order_count = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    construction_button = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    check_text_on_construction_page = (By.CSS_SELECTOR, 'h1.text.text_type_main-large.mb-5.mt-10')

class Construction:
    first_ingredient = (By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]')
    bay_burger = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img')
    check_text_details_ingredient = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    close_ingredient_window = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    check_ingredient_count = (By.XPATH, "//*[contains(@class, 'totalContainer')]")
    basket = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul')
    click_order = (By.XPATH, "//*[text()='Оформить заказ']")
    check_text_successful_order = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')
    constructor = (By.XPATH,"//*[text()='Конструктор']")

class OrderFeed:
    first_order = (By.CLASS_NAME, "OrderHistory_dataBox__1mkxK")
    check_text_details_order = (By.XPATH, "//*[text()='Cостав']")
    indicator_count_order = (By.XPATH, "//*[contains(@class, 'title_shadow')]")
    indicator_count_order_in_personal_account = (By.XPATH, "(//*[contains(@class, 'OrderHistory_textBox')])[last()]")
    count_all_time = (By.XPATH, "//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large'][1]")
    count_today = (By.XPATH,"//*[contains(text(),'Выполнено за сегодня:')]")
    close_modal_wind = (By.XPATH, "//*[contains(@class, 'modal__close')]")
    order_in_progress = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")

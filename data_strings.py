from enum import Enum


class DataStrings(str, Enum):
    pick_burger = 'Соберите бургер'
    ingredient_details = 'Детали ингредиента'
    your_order_started_to_prepare = "Ваш заказ начали готовить"
    window_not_closed = 'Окно не закрылось'
    structure = 'Cостав'
    default_order_number = "9999"
    you_can_change_your_personal_data = "В этом разделе вы можете изменить свои персональные данные"
    completed = "Выполнен"
    recover_password = "Восстановить пароль"
    password_recovery = "Восстановление пароля"
    enter_code_from_email = "Введите код из письма"

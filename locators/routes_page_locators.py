from selenium.webdriver.common.by import By

PIN = lambda adr: f"//ymaps[contains(text(), '{adr}')]"
MODE = lambda mode: f"//div[contains(@class, 'modes-container')]/div[contains(text(), '{mode}')]"
TYPE = lambda type: f"//div[contains(@class, 'types-container')]/div[./img[contains(@src,'{type}')]]"
TARIFF = lambda fare: f"//div[contains(@class, 'tariff-cards')]/div[./div[contains(text(), '{fare}')]]"

class RoutesPageLocators:
    from_input = (By.XPATH, "//div[./label[contains(text(), 'Откуда')]]/input")
    to_input = (By.XPATH, "//div[./label[contains(text(), 'Куда')]]/input")
    PIN_BY_ADR = lambda adr: (By.XPATH, PIN(adr))
    type_picker_modal = (By.XPATH, "//div[contains(@class, 'type-picker shown')]")
    result_text = (By.XPATH, "//div[contains(@class, 'type-picker shown')]//div[@class= 'text']")
    result_duration = (By.XPATH, "//div[contains(@class, 'type-picker shown')]//div[@class= 'duration']")
    result_button=(By.XPATH, "//div[contains(@class, 'type-picker shown')]//button")
    MODE_BY_NAME = lambda mode: (By.XPATH, MODE(mode))
    TYPE_BY_NAME = lambda type: (By.XPATH, TYPE(type))
    TARIFF_BY_NAME = lambda fare: (By.XPATH, TARIFF(fare))
    TARIIF_INFO = lambda fare: (By.XPATH, f"{TARIFF(fare)}/button")
    TARIIF_DESCRIPTION = lambda fare: (By.XPATH, f"{TARIFF(fare)}//div[contains(@class, 'i-dPrefix')]")
    number_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Телефон')]")
    payment_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Способ оплаты')]")
    comment_input = (By.XPATH, "//div[contains(@class, 'form')]//div[./label[contains(text(), 'Комментарий водителю...')]]")
    req_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Требования к заказу')]")
    submit_button = (By.XPATH, "//button[./span[contains(text(), 'Ввести номер и заказать')]]")

    notbook_table_switch = (By.XPATH, "//div[contains(@class, 'form')]//div[./div[contains(text(), 'Столик для ноутбука')]]//div[contains(@class, 'switch')]")

    """
    number_input = (By.XPATH, "//input[contains(@id, 'phone')]")
    number_submit = (By.XPATH, "//div[./div[contains(text(), 'Введите номер телефона')]]//button[contains(text(), 'Далее')]")
    signup_button = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    signin_button = (By.XPATH, "//a[contains(text(), 'Войти')]")
    signout_button = (By.XPATH, "//a[contains(text(), 'Выход')]")
    recipes_button = (By.XPATH, "//a[contains(text(), 'Рецепты')]")
    create_recipe_button = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
"""
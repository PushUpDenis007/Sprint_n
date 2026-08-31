from selenium.webdriver.common.by import By

PIN = lambda adr: f"//ymaps[contains(text(), '{adr}')]"
MODE = lambda mode: f"//div[contains(@class, 'modes-container')]/div[contains(text(), '{mode}')]"
TYPE = lambda type: f"//div[contains(@class, 'types-container')]/div[./img[contains(@src,'{type}')]]"
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
#
    """
    signup_button = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    signin_button = (By.XPATH, "//a[contains(text(), 'Войти')]")
    signout_button = (By.XPATH, "//a[contains(text(), 'Выход')]")
    recipes_button = (By.XPATH, "//a[contains(text(), 'Рецепты')]")
    create_recipe_button = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
"""
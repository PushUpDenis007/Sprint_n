from selenium.webdriver.common.by import By

PIN = lambda adr: f"//ymaps[contains(text(), '{adr}')]"
class RoutesPageLocators:
    from_input = (By.XPATH, "//div[./label[contains(text(), 'Откуда')]]/input")
    to_input = (By.XPATH, "//div[./label[contains(text(), 'Куда')]]/input")
    PIN_BY_ADR = lambda adr: (By.XPATH, PIN(adr))
    type_picker_modal = (By.XPATH, "//div[contains(@class, 'type-picker shown')]")
    result_text = (By.XPATH, "//div[contains(@class, 'type-picker shown')]//div[@class= 'text']")
    result_duration = (By.XPATH, "//div[contains(@class, 'type-picker shown')]//div[@class= 'duration']")
    """
    signup_button = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    signin_button = (By.XPATH, "//a[contains(text(), 'Войти')]")
    signout_button = (By.XPATH, "//a[contains(text(), 'Выход')]")
    recipes_button = (By.XPATH, "//a[contains(text(), 'Рецепты')]")
    create_recipe_button = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
"""
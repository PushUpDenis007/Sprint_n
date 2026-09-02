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
    TARIFF_PRICE = lambda fare: (By.XPATH, f"{TARIFF(fare)}/div[contains(@class, 'tcard-price')]")
    TARIIF_INFO = lambda fare: (By.XPATH, f"{TARIFF(fare)}/button")
    TARIIF_DESCRIPTION = lambda fare: (By.XPATH, f"{TARIFF(fare)}//div[contains(@class, 'i-dPrefix')]")
    number_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Телефон')]")
    payment_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Способ оплаты')]")
    comment_input = (By.XPATH, "//div[contains(@class, 'form')]//div[./label[contains(text(), 'Комментарий водителю...')]]")
    req_button = (By.XPATH, "//div[contains(@class, 'form')]//div[contains(text(), 'Требования к заказу')]")
    submit_button = (By.XPATH, "//button[./span[contains(text(), 'Ввести номер и заказать')]]")
    notbook_table_switch = (By.XPATH, "//div[contains(@class, 'form')]//div[./div[contains(text(), 'Столик для ноутбука')]]//div[contains(@class, 'switch')]")

    search_taxi_modal = (By.XPATH, "//div[contains(@class, 'order-body')]")
    search_taxi_header = (By.XPATH, "//div[contains(text(), 'Поиск машины')]")
    search_taxi_timer = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    search_taxi_cancel_button = (By.XPATH, "//div[text()='Отменить']/preceding-sibling::button[@class='order-button']")
    search_taxi_details_button = (By.XPATH, "//div[text()='Детали']/preceding-sibling::button[@class='order-button']")
    search_taxi_price_label = (By.XPATH, "//div[contains(text(), 'Еще про поездку')]/following-sibling::div") 

    final_taxi_time = (By.XPATH, "//div[contains(@class, 'order-body')]//div[contains(@class, 'order-header-title')]")
    final_taxi_number = (By.XPATH, "//div[contains(@class, 'order-number')]//div[contains(@class, 'number')]")
    final_taxi_image = (By.XPATH, "//div[contains(@class, 'order-number')]//img[contains(@alt, 'Car')]")
    final_taxi_driver_name = (By.XPATH, "//div[contains(@class, 'order-button')]//div[contains(@class, 'order-button')]/following-sibling::div")
    final_taxi_driver_photo = (By.XPATH, "//div[contains(@class, 'order-button')]//div[contains(@class, 'order-button')]//img")
    final_taxi_driver_raiting = (By.XPATH, "//div[contains(@class, 'order-button')]//div[contains(@class, 'order-button')]//div[contains(@class, 'order-btn-rating')]")
from locators.routes_page_locators import RoutesPageLocators as Routes
from pages.base_page import BasePage
import allure



class RoutesPage(BasePage):

    @allure.step('Заполнить поле Откуда')
    def fill_from_input (self,adr):
        self.wait_for_clickable(Routes.from_input)
        self.send_keys(Routes.from_input,adr)

    @allure.step('Заполнить поле Куда')
    def fill_to_input (self,adr):
        self.wait_for_clickable(Routes.to_input)
        self.send_keys(Routes.to_input,adr)   

    @allure.step('Проверить наличие пина {adr} на карте')
    def check_pin_on_map (self,adr):
        return self.wait_for_visibility(Routes.PIN_BY_ADR(adr))   

    @allure.step('Проверить наличие блока с выбором маршрута')
    def check_type_modal_exist (self):
        return self.wait_for_visibility(Routes.type_picker_modal)   

    @allure.step('Получить текст блока с выбором маршрута')
    def get_result_text (self):
        return self.get_text(Routes.result_text)

    @allure.step('Получить длительность блока с выбором маршрута')
    def get_result_duration (self):
        return self.get_text(Routes.result_duration)

    @allure.step('Изменить таб на {mode}')
    def change_mode (self,mode):
        self.wait_for_clickable(Routes.MODE_BY_NAME(mode))
        self.click_element (Routes.MODE_BY_NAME(mode))

    @allure.step('Получить атрибут таба {mode}')
    def get_mode_attribute (self,mode):
        return self.get_attribute(Routes.MODE_BY_NAME(mode),'class')

    @allure.step('Изменить тип дживения на {type}')
    def change_type (self,type):
        self.wait_for_clickable(Routes.TYPE_BY_NAME(type))
        self.click_element (Routes.TYPE_BY_NAME(type))

    @allure.step('Изменить тип тариф на {tariff}')
    def change_tariff (self,tariff):
        self.wait_for_clickable(Routes.TARIFF_BY_NAME(tariff[0]))
        self.click_element (Routes.TARIFF_BY_NAME(tariff[0]))

    @allure.step('Получить атрибут типа движения {type}')
    def get_type_attribute (self,type):
        return self.get_attribute(Routes.TYPE_BY_NAME(type),'class')

    @allure.step('Проверить что типы движения активны')
    def is_types_active (self,*type):
        for t in type:
            if "disabled" in (self.get_type_attribute(t) or ''):
                return False
        return True

    @allure.step('Нажать кнопку Вызвать заказ')
    def click_result_button (self):
        return self.click_element(Routes.result_button)    
       
    @allure.step('Получить текст кнопки заказа')
    def get_result_button_text (self):
        return self.get_text(Routes.result_button)    

    @allure.step('Проверить что кнопка заказа активна')
    def result_button_is_active (self, text):
        return (self.wait_for_clickable(Routes.result_button) and self.get_text(Routes.result_button) == text)

    @allure.step('Проверить что кнопка заказа активна')
    def is_exist_and_any_active(self, *tariffs):
        is_active = 0
        for t in tariffs:
            element = self.find_element(Routes.TARIFF_BY_NAME(t[0]))
            if "active" in element.get_attribute("class"):
                is_active += 1
        return is_active == 1

    @allure.step('Проверить описание в окне инфо')
    def check_info_description (self,tariff):
        self.wait_for_located(Routes.TARIFF_BY_NAME(tariff[0]))
        self.click_element(Routes.TARIFF_BY_NAME(tariff[0]))
        self.wait_for_located(Routes.TARIIF_INFO(tariff[0]))
        self.hover_on_element(Routes.TARIIF_INFO(tariff[0]))
        self.wait_for_located(Routes.TARIIF_DESCRIPTION(tariff[0]))
        return self.get_text(Routes.TARIIF_DESCRIPTION(tariff[0])) == tariff[1]

    @allure.step('Проверить что поле Телефон оторбажается')
    def is_number_button_visible (self):
        return self.wait_for_visibility (Routes.number_button)

    @allure.step('Проверить что поле Способ оплаты оторбажается')
    def is_payment_button_visible (self):
        return self.wait_for_visibility (Routes.payment_button)

    @allure.step('Проверить что поле Комментарий водителю оторбажается')
    def is_comment_input_visible (self):
        return self.wait_for_visibility (Routes.comment_input)

    @allure.step('Проверить что поле Требования к заказу оторбажается')
    def is_req_button_visible (self):
        return self.wait_for_visibility (Routes.req_button)

    @allure.step('Проверить что Кнопка финального заказа оторбажается')
    def is_submit_button_visible (self):
        return self.wait_for_visibility (Routes.submit_button)  

    @allure.step('Активировать чекбокс Столик для ноутбука')
    def click_checkbox_notebook_table (self):
        self.wait_for_located(Routes.req_button)
        self.click_element(Routes.req_button)
        self.wait_for_located (Routes.notbook_table_switch)
        return self.click_element (Routes.notbook_table_switch)  

    @allure.step('Нажимаем кнопку Ввести номер и заказать')
    def click_submit_button (self):
        self.wait_for_located (Routes.submit_button)
        return self.click_element (Routes.submit_button)   

    @allure.step('Проверить что окно ожиания такси корректно')
    def is_search_taxi_modal_correct (self):
        self.wait_for_located(Routes.search_taxi_header)
        self.wait_for_located(Routes.search_taxi_timer)
        self.wait_for_located(Routes.search_taxi_cancel_button)
        self.wait_for_located(Routes.search_taxi_details_button)
        return True

    @allure.step('Дождаться такси')
    def is_taxi_found (self,time):
        return self.wait_for_located(Routes.final_taxi_number, time)

    @allure.step('Дождаться такси')
    def is_taxi_found_modal_correct (self):
        self.wait_for_located(Routes.final_taxi_time)
        self.wait_for_located(Routes.final_taxi_number)
        self.wait_for_located(Routes.final_taxi_image)
        self.wait_for_located(Routes.final_taxi_driver_name)
        self.wait_for_located(Routes.final_taxi_driver_photo)
        self.wait_for_located(Routes.final_taxi_driver_raiting)
        self.wait_for_located(Routes.search_taxi_details_button)
        self.wait_for_located(Routes.search_taxi_cancel_button)
        return True

    @allure.step('Проверить что картинка авто в заказе совпадает с картинкой тарифа')
    def is_img_tarrif_correct (self,tariff):
        self.wait_for_located(Routes.final_taxi_image)
        return tariff[2] in self.get_attribute(Routes.final_taxi_image,"src")

    @allure.step('Нажимаем кнопку Детали')
    def click_order_details_button (self):
        self.wait_for_located (Routes.search_taxi_details_button)
        return self.click_element (Routes.search_taxi_details_button)   

    @allure.step('Узнать стоимость тарифа')
    def get_tariff_price (self,tariff):
        self.wait_for_located (Routes.TARIFF_PRICE(tariff[0]))
        return self.get_text(Routes.TARIFF_PRICE(tariff[0])).replace("₽", "").strip()

    @allure.step('Узнать стоимость тарифа')
    def get_order_cost (self):
        self.wait_for_located (Routes.search_taxi_price_label)
        return self.get_text(Routes.search_taxi_price_label).split("-")[1].replace("₽", "").strip()
    
    @allure.step('Нажимаем кнопку Отмена')
    def click_order_cancel_button (self):
        self.wait_for_located (Routes.search_taxi_cancel_button)
        return self.click_element (Routes.search_taxi_cancel_button)   

    @allure.step('Проверить оствутвие модалки заказа')
    def is_order_modal_visible (self):
        return self.wait_for_invisibility(Routes.search_taxi_modal)
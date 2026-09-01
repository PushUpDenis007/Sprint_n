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

    @allure.step('открыть инфо тарифа')
    def click_info_tariff_button (self,tariff):
        self.wait_for_located(Routes.TARIIF_INFO(tariff[0]))
        return self.click_element(Routes.TARIIF_INFO(tariff[0]))    

    @allure.step('Проверить описание в окне инфо')
    def check_info_description (self,tariff):
        self.wait_for_located(Routes.TARIFF_BY_NAME(tariff[0]))
        self.click_element(Routes.TARIFF_BY_NAME(tariff[0]))
        self.wait_for_located(Routes.TARIIF_INFO(tariff[0]))
        self.click_element(Routes.TARIIF_INFO(tariff[0]))
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
    
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
        
    @allure.step('Получить текст кнопки заказа')
    def get_result_button_text (self):
        return self.get_text(Routes.result_button)    

    @allure.step('Проверить что кнопка заказа активна')
    def result_button_is_active (self, text):
        return (self.wait_for_clickable(Routes.result_button) and self.get_text(Routes.result_button) == text)
"""
    @allure.step('Нажать на кнопку в шапке Войти')
    def click_signin_button (self):
        self.click_element(Base.signin_button) 

    @allure.step('Заполнить почту')
    def fill_email_input (self,email):
        self.send_keys (Signin.email_input,email)

    @allure.step('Заполнить пароль')
    def fill_pass_input (self,password):
        self.send_keys(Signin.password_input,password)

    @allure.step('Дождаться появления кнопки Вход')
    def locate_confirm_button(self):
        return self.wait_for_located(Signin.confirm_button)
    
    @allure.step('Нажать на кнопку подтверждения Входа')
    def click_signin_confirm_button (self):
        self.click_element(Signin.confirm_button)    

    @allure.step('Дождаться появления кнопки Выход')
    def locate_signout_button (self):
        return self.wait_for_located (Base.signout_button)
"""
    
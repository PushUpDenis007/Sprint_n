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
    
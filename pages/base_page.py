from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Дождать когда элемент станет кликабельным')
    def wait_for_clickable(self,locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))     

    @allure.step('Дождать когда элемент появится на странице')
    def wait_for_located(self,locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Дождать когда элемент станет видимым')
    def wait_for_visibility(self,locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Дождать когда появится атрибут')
    def wait_for_attribute_to_contain(self, locator, attribute, value):
        try:
            WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))
            return True
        except:
            return False        

    @allure.step('Дождать когда элемент станет невидимым')
    def wait_for_invisibility(self,locator):
        return WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(locator)) 

    @allure.step('Получить текст')
    def get_text(self,locator):
        return self.find_element(locator).text

    @allure.step('Отправить текст "{text}"')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
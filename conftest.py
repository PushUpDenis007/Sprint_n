import pytest, allure
from pages.routes_page import RoutesPage
from urls import Urls
from webdriver_factory import WebDriverFactory
from locators.routes_page_locators import RoutesPageLocators as Routes
from data import Adresses as Adr

def pytest_addoption(parser):
    """Регистрируем параметр командной строки для выбора браузера."""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Браузер для тестов: chrome, firefox"
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    allure.dynamic.parameter("Браузер", browser_name.upper())
    with allure.step(f'Открываем сайт в браузере {browser_name.upper()}'):
        driver = WebDriverFactory.get_driver(browser_name)
        driver.get(Urls.BASE_URL)
    yield driver
    with allure.step('Закрываем сайт'):
        driver.quit()

@pytest.fixture
def fill_from_to(routes_page):
    routes_page.fill_from_input(Adr.ADRESS1)
    routes_page.fill_to_input(Adr.ADRESS2)

@pytest.fixture
def routes_page(driver):
    return RoutesPage(driver)

"""
@pytest.fixture
def registration (driver):
    payload = create_user_payload()
    signup_page = SignupPage(driver)
    signup_page.click_signup_button()
    signup_page.wait_for_located (Signup.email_input)
    signup_page.fill_first_name_input(payload ["name"])
    signup_page.fill_last_name_input(payload ["last_name"])
    signup_page.fill_username_input(payload["username"])
    signup_page.fill_email_input(payload["email"])
    signup_page.fill_pass_input(payload["password"])
    signin_page = signup_page.click_signup_confirm_button()
    signin_page.locate_confirm_button()
    return payload

@pytest.fixture
def login(driver,registration):
    signin_page = SigninPage(driver)
    signin_page.fill_email_input(registration["username"])
    signin_page.fill_pass_input(registration ["password"])
    signin_page.click_signin_confirm_button()
    signin_page.locate_signout_button()

    


@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)
    """
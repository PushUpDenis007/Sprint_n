import pytest, allure
from pages.routes_page import RoutesPage
from urls import Urls
from webdriver_factory import WebDriverFactory
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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import config, os

class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name: str):
        browser_name = browser_name.lower().strip()
        selenoid_url = os.environ.get("SELENOID_URL")
        if selenoid_url:
            # Режим работы в Docker / CI через Selenoid
            if browser_name == "chrome":
                options = ChromeOptions()
                return webdriver.Remote(command_executor=selenoid_url, options=options)
            elif browser_name == "firefox":
                options = FirefoxOptions()
                return webdriver.Remote(command_executor=selenoid_url, options=options)
            else:
                raise ValueError(f"Браузер '{browser_name}' не поддерживается в Selenoid.")

        else:
            if browser_name == "chrome":
                options = ChromeOptions()
                options.binary_location = config.CHROME_PATH
                service = ChromeService(executable_path=config.DRIVER_PATH)
                return webdriver.Chrome(service=service, options=options)
            elif browser_name == "firefox":
                return webdriver.Firefox()
            elif browser_name == "edge":
                return webdriver.Edge()
            else:
                raise ValueError(f"Браузер '{browser_name}' не поддерживается фабрикой.")

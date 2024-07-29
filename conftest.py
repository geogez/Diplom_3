import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Urls.urls import Urls


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    if browser_name == 'chrome':
        # Установка и запуск ChromeDriver
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser_name == 'firefox':
        # Установка и запуск GeckoDriver (FirefoxDriver)
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    else:
        raise ValueError("Unsupported browser! Please choose 'chrome' or 'firefox'.")

    # Настройки драйвера
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    driver.get(Urls.main_page)

    yield driver

    driver.quit()

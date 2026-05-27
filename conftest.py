import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def driver_scope_class(request):
    with allure.step('Открываем браузер Firefox'):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)

    request.cls.driver = driver

    yield driver

    with allure.step('Закрываем браузер Firefox'):
        driver.quit()


@pytest.fixture()
def driver():
    with allure.step('Открываем браузер Firefox'):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        driver.implicitly_wait(10)

    yield driver

    with allure.step('Закрываем браузер Firefox'):
        driver.quit()


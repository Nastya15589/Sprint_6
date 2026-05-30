from datetime import datetime

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class OrderPage(BasePage):
    order_button_header = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    order_button_main = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button")
    name_field = (By.XPATH, ".//input[@placeholder='* Имя']")
    last_name_field = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    metro_station_first = (By.XPATH, ".//li[@data-value='1']")
    number_field = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    continue_button = (By.XPATH, ".//button[text()='Далее']")
    delivery_date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    rental_period_day = (By.XPATH, "(.//div[@role='option'])[1]")
    order_button = (By.XPATH, "(.//button[text()='Заказать'])[2]")
    confirmation_button = (By.XPATH, ".//button[text()='Да']")
    successful_order_status = (By.XPATH, ".//div[text()='Заказ оформлен']")
    logo_yandex = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    main_page_title = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    accept_cookies = (By.XPATH, ".//button[@id='rcc-confirm-button']")

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self, locator):
        self.click_element(locator)

    @allure.step('Нажать кнопку Принять cookie')
    def click_accept_cookies_button(self):
        self.click_element(self.accept_cookies)

    @allure.step('Ввести имя')
    def set_name(self, name):
        self.set_value(self.name_field, name)

    @allure.step('Ввести фамилию')
    def set_last_name(self, last_name):
        self.set_value(self.last_name_field, last_name)

    @allure.step('Ввести адрес')
    def set_address(self, address):
        self.set_value(self.address_field, address)

    @allure.step('Нажать на dropdown станций метро')
    def click_metro_station(self):
        self.click_element(self.metro_station)

    @allure.step('Выбрать станцию метро')
    def select_metro_station_first(self):
        self.click_element(self.metro_station_first)

    @allure.step('Ввести номер телефона')
    def set_number(self, number):
        self.set_value(self.number_field, number)

    @allure.step('Нажать кнопку продолжить')
    def click_continue_button(self):
        self.click_element(self.continue_button)

    @allure.step('Выбрать дату доставки')
    def set_delivery_date(self):
        today = datetime.now().date()
        self.set_value(self.delivery_date, str(today))

    @allure.step('Нажать на dropdown срока аренды')
    def click_rental_period(self):
        self.click_element(self.rental_period)

    @allure.step('Выбрать срок аренды')
    def select_rental_period_day(self):
        self.click_element(self.rental_period_day)

    @allure.step('Нажать на кнопку заказать')
    def place_order_button(self):
        self.click_element(self.order_button)

    @allure.step('Нажать на кнопку Подтверждения заказа')
    def click_confirmation_button(self):
        self.click_element(self.confirmation_button)

    @allure.step('Отображение успешного статуса заказа')
    def check_successful_order_status(self):
        try:
            self.find_element(self.successful_order_status)
            return True

        except TimeoutException:
            return False

    @allure.step('Нажать на логотип самоката')
    def click_logo_scooter(self):
        self.click_element(self.logo_scooter)

    @allure.step('Нажать на логотип яндекса')
    def click_logo_yandex(self):
        self.click_element(self.logo_yandex)

    @allure.step('Проверить отображение заголовка на главной странице')
    def check_appearance_main_page_title(self):
        try:
            self.find_element(self.main_page_title)
            return True

        except TimeoutException:
            return False




    def set_client_data(self, name, last_name, address, number):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.click_metro_station()
        self.select_metro_station_first()
        self.set_number(number)
        self.click_continue_button()

    def set_rental_data(self):
        self.set_delivery_date()
        self.click_rental_period()
        self.select_rental_period_day()
        self.place_order_button()
        self.click_confirmation_button()


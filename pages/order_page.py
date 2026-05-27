from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
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


    def __init__(self,driver):
        self.driver = driver

    def click_order_button(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def click_accept_cookies_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_cookies)).click()

    def set_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_field)).send_keys(name)

    def set_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_field)).send_keys(
            last_name)

    def set_address(self, address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address_field)).send_keys(
            address)

    def click_metro_station(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.metro_station)).click()

    def select_metro_station_first(self ):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.metro_station_first)).click()

    def set_number(self, number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.number_field)).send_keys(number)

    def click_continue_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()

    def set_delivery_date(self):
        today = datetime.now().date()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.delivery_date)).send_keys(str(today))

    def click_rental_period(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.rental_period)).click()

    def select_rental_period_day(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.rental_period_day)).click()

    def place_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button)).click()

    def click_confirmation_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirmation_button)).click()

    def check_successful_order_status(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.successful_order_status))
            return True

        except TimeoutException:
            return False

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logo_scooter)).click()

    def click_logo_yandex(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logo_yandex)).click()

    def check_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url

    def check_appearance_main_page_title(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main_page_title))
            return True

        except TimeoutException:
            return False

    def switch_new_window(self, main_window):

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)


        for window in self.driver.window_handles:
            if window != main_window:
                self.driver.switch_to.window(window)
                break


        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )


        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )


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


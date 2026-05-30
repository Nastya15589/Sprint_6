from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_text(self,locator):
        element = self.find_element(locator)
        return element.text

    def click_question(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def set_value(self,locator,value):
        element = self.find_element(locator)
        element.send_keys(value)

    def check_url(self):
        current_url = self.driver.current_url
        return current_url

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def open_url(self, url):
        self.driver.get(url)

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

    def current_window(self):
        return self.driver.current_window_handle
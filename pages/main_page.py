from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    questions_about_important = [By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and text() = 'Вопросы о важном']"]
    first_question = (By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']")
    first_question_answer = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    second_question = (By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']")
    second_question_answer = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    third_question = (By.XPATH, ".//div[text()='Как рассчитывается время аренды?']")
    third_question_answer = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    fourth_question = (By.XPATH, ".//div[@id='accordion__heading-3']")
    fourth_question_answer = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    fifth_question = (By.XPATH, ".//div[@id='accordion__heading-4']")
    fifth_question_answer = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    sixth_question = (By.XPATH, ".//div[@id='accordion__heading-5']")
    sixth_question_answer = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    seventh_question = (By.XPATH, ".//div[@id='accordion__heading-6']")
    seventh_question_answer = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    eighth_question = (By.XPATH, ".//div[@id='accordion__heading-7']")
    eighth_question_answer = (By.XPATH, ".//div[@id='accordion__panel-7']/p")


    def __init__(self,driver):
        self.driver = driver

    def scroll_to_questions_about_important(self):
        element = self.driver.find_element(*self.questions_about_important)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()


    def find_text_question(self, locator_text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_text))
        actual_result = element.text
        return actual_result



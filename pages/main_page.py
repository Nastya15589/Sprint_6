import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    questions_about_important = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and text() = 'Вопросы о важном']")
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
    accept_cookies = (By.XPATH, ".//button[@id='rcc-confirm-button']")

    @allure.step('Скроллим страницу до Вопросы о важном')
    def scroll_to_questions_about_important(self):
        self.scroll_to_element(self.questions_about_important)

    @allure.step('Нажимаем каждый вопрос')
    def click_questions(self, locator):
        self.click_question(locator)

    @allure.step('Находим и получаем текст каждого вопроса')
    def find_text_question(self, locator):
        return self.get_text(locator)




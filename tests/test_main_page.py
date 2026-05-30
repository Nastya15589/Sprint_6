import allure
import pytest

from pages.main_page import MainPage
import data as d


class TestMainPage:

    @allure.title('Проверка соответствия текста каждому вопросу')
    @allure.description('На странице раскрываем каждый вопрос и проверяем текст')
    @pytest.mark.parametrize('locator,text,expected_result', d.test_data)
    def test_question(self, driver_scope_class, locator, text, expected_result):
        driver_scope_class.get(d.Urls.main_rage_url)
        main_page = MainPage(driver_scope_class)
        main_page.scroll_to_questions_about_important()
        main_page.click_questions(locator)
        actual_result = main_page.find_text_question(text)
        assert actual_result == expected_result



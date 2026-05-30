import allure
import pytest

from pages.order_page import OrderPage
import data as d


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @allure.description('Заказать самокат через обе кнопки')
    @pytest.mark.parametrize('button_locator,name,last_name,address,number', d.test_set)

    def test_order_scooter_success(self, driver,button_locator, name,last_name,address,number):

        driver.get(d.Urls.main_rage_url)
        order_page = OrderPage(driver)
        order_page.click_accept_cookies_button()
        order_page.click_order_button(button_locator)
        order_page.set_client_data(name,last_name,address,number)
        order_page.set_rental_data()

        assert order_page.check_successful_order_status()

        driver.refresh()
        order_page.click_logo_scooter()
        assert order_page.check_appearance_main_page_title()

        main_window = order_page.current_window()
        order_page.click_logo_yandex()
        order_page.switch_new_window(main_window)
        assert "yandex.kz" in order_page.check_url()

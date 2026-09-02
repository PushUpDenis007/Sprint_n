from data import Modes, Tariff
import allure,pytest

@allure.feature("Заказ тарифа Такси.")
class TestOrderTaxiRoute:
    @allure.title("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_call_taxi_six_types_shown (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        assert routes_page.is_exist_and_any_active (Tariff.WORK, Tariff.SLEEPY, Tariff.HOLIDAY, Tariff.CHATTY, Tariff.COMFORT, Tariff.GLOSSY)

    @pytest.mark.xfail(reason="Некорректное описание у тарифов Сонный и Разговорчивый")    
    @pytest.mark.parametrize("tariffs_list", [Tariff.WORK, Tariff.SLEEPY, Tariff.HOLIDAY, Tariff.CHATTY, Tariff.COMFORT, Tariff.GLOSSY])
    @allure.title("При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ")
    def test_info_button_info_shown (self,routes_page,fill_from_to,tariffs_list):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        assert routes_page.check_info_description (tariffs_list)

    @allure.title("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси.")
    def test_call_taxi_fields_shown (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        assert routes_page.is_number_button_visible()
        assert routes_page.is_payment_button_visible()
        assert routes_page.is_comment_input_visible()
        assert routes_page.is_req_button_visible()
        assert routes_page.is_submit_button_visible()
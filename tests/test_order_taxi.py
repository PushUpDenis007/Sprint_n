from data import Modes, Types, Buttons, Tariff
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
"""
    @pytest.mark.xfail(reason="Время Оптимального и Быстрого маршрутов совпадает (3 мин.)")
    @allure.title("Проверка смена активного таба и пересчет времени и стоимости маршрута")
    def test_change_mode_mode_changed (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.OPTIMAL)
        optimal_active = routes_page.get_mode_attribute(Modes.OPTIMAL)
        optimal_text = routes_page.get_result_text()
        optimal_duration = routes_page.get_result_duration()
        routes_page.change_mode(Modes.FAST)
        assert "active" in optimal_active
        assert "active" in routes_page.get_mode_attribute(Modes.FAST)
        assert routes_page.get_result_text() != optimal_text
        assert routes_page.get_result_duration() != optimal_duration

    @allure.title("При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения")
    def test_change_mode_custom_types_active (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.CUSTOM)
        assert "active" in routes_page.get_mode_attribute(Modes.CUSTOM)
        assert routes_page.is_types_active(Types.CAR,Types.WALK,Types.TAXI, Types.BIKE, Types.SCOOTER, Types.DRIVE)

    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_fast_mode_active_button (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        assert routes_page.result_button_is_active(Buttons.TAXI)

    @allure.title("При выборе вида маршрута Свой активна кнопка Вызвать такси")
    def test_custom_mode_active_button (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.CUSTOM)
        routes_page.change_type(Types.DRIVE)
        assert routes_page.result_button_is_active(Buttons.DRIVE)    
"""
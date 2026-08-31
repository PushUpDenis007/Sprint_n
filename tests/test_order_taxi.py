from data import Modes, Types, Buttons
import allure,pytest

@allure.feature("Заказ тарифа Такси.")
class TestOrderTaxiRoute:
    @allure.title("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_change_mode_custom_types_active (self,routes_page,fill_from_to):
        pass

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
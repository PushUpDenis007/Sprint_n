from data import Modes, Types, Buttons, Tariff
import allure,pytest

@allure.feature("Сценарий. Ввести два разных предустановленных адреса в поля Откуда и Куда, выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
class TestFullScenarioRoute:

    @allure.title("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины")
    def test_submit_taxi_search_modal_shown (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        routes_page.change_tariff(Tariff.WORK)
        routes_page.click_checkbox_notebook_table()
        routes_page.click_submit_button()
        assert routes_page.is_search_taxi_modal_correct()

    @allure.title("Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа")
    def test_find_taxi_order_complete_shown (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        routes_page.change_tariff(Tariff.WORK)
        routes_page.click_checkbox_notebook_table()
        routes_page.click_submit_button()
        routes_page.is_taxi_found(60)
        assert routes_page.is_taxi_found_modal_correct()
        assert routes_page.is_img_tarrif_correct(Tariff.WORK)

    @allure.title("Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа")
    def test_order_details_cost_tariff (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        routes_page.change_tariff(Tariff.WORK)
        tariff_price = routes_page.get_tariff_price(Tariff.WORK)
        routes_page.click_submit_button()
        routes_page.click_order_details_button()
        order_cost = routes_page.get_order_cost()
        assert tariff_price == order_cost

    @allure.title("Нажать кнопку Отмена - Окно закрывается")
    def test_click_cancel_modal_closed (self,routes_page,fill_from_to):
        routes_page.change_mode(Modes.FAST)
        routes_page.click_result_button()
        routes_page.change_tariff(Tariff.WORK)
        routes_page.click_submit_button()
        routes_page.click_order_cancel_button()
        assert routes_page.is_order_modal_visible()
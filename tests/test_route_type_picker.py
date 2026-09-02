from data import Adresses as Adr
import allure

@allure.feature("Отрисовка блока с выбором маршрута")
class TestTypeRoute:

    @allure.title("Проверка Отрисовка блока с выбором маршрута с разными адресами")
    def test_fill_diff_adr_type_modal_shown (self,routes_page):
        routes_page.fill_from_input(Adr.ADRESS1)
        routes_page.fill_to_input(Adr.ADRESS2)
        assert routes_page.check_type_modal_exist()

    @allure.title("Проверка Отрисовка блока с выбором маршрута с одинаковыми адресами")
    def test_fill_same_adr_text_free_duration_zero (self,routes_page):
        routes_page.fill_from_input(Adr.ADRESS1)
        routes_page.fill_to_input(Adr.ADRESS1)
        assert "Бесплатно" in routes_page.get_result_text()
        assert "В пути 0 мин" in routes_page.get_result_duration()
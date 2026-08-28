from data import Adresses as Adr
import allure

@allure.feature("Отрисовка маршрута")
class TestCommonPrintRoutes:

    @allure.title("Проставя првоерка Отрисовка маршрута")
    def test_fill_inputs_pins_on_map (self,routes_page):
        routes_page.fill_from_input(Adr.ADRESS1)
        routes_page.fill_to_input(Adr.ADRESS2)
        assert routes_page.check_pin_on_map(Adr.ADRESS1)
        assert routes_page.check_pin_on_map(Adr.ADRESS2)
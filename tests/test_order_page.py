from fixtures.constants import OrderMessages


class TestLoginPage:
    def test_order_hotel(self, app):
        """
        Test for valid booking.

        :notes: Test 24.
        """
        app.order_page.open_login_page()
        username = "test"
        password = "testtesttest"
        app.order_page.login(username=username, password=password)
        app.order_page.button_click()
        assert app.order_page.element_first_card_on_list_of_accommodation()
        app.order_page.button_click()
        assert app.order_page.element_accommodation_details()
        app.order_page.button_click()
        app.order_page.enter_on_basket_page()
        assert app.order_page.text_on_baskets_header() == OrderMessages.BASKETS_HEADER
        app.order_page.enter_in_order_to_the_design()
        assert app.order_page.text_on_order_create() == OrderMessages.NEW_ORDER
        app.order_page.order_save()
        assert app.order_page.text_on_your_order() == OrderMessages.YOUR_ORDER

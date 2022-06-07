import logging
import pytest
from fixtures.constants import LogMessages
from tests.constants_test_cases import DataCasesPasswords


class TestLoginPage:
    def test_valid_login(self, app):
        """
        Test for valid logging.

        :notes: Test 19.
        """
        app.login_page.open_login_page()
        username = "test"
        password = "testtesttest"
        app.login_page.login(username=username, password=password)
        assert app.login_page.see_accommodation_main_page

    @pytest.mark.parametrize("username_data, pass_data", DataCasesPasswords.INVALID_EMPTY_DATA_FOR_LOG_PAGE)
    def test_invalid_login_empty(self, app, username_data, pass_data):
        """
        Test for invalid logging with empty data.

        :notes: Test 20, 21.
        """
        app.login_page.open_login_page()
        username = username_data
        password = pass_data
        app.login_page.login(username=username, password=password)
        assert app.login_page.text_on_head_in_log_in_page() == LogMessages.LOG_IN

    @pytest.mark.parametrize("username_data, pass_data", DataCasesPasswords.INVALID_DATA_FOR_LOG_PAGE)
    def test_invalid_login_invalid(self, app, username_data, pass_data):
        """
        Test for invalid logging with invalid data.

        :notes: Test 22, 23.
        """
        app.login_page.open_login_page()
        username = username_data
        password = pass_data
        app.login_page.login(username=username, password=password)
        all_errors_msgs = app.login_page.text_many_errors_login_page()
        assert LogMessages.ERROR_USERNAME_OR_PASS in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}")

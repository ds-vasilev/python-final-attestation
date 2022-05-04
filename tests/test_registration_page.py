import pytest
import logging
from random import randint
from fixtures.constants import RegMessages
from models.register import RegisterUserModel
from tests.constants_test_cases import TestCases
import time
# import json
# from selenium.webdriver.common.by import By



class TestRegistrationPage:
    def test_valid_register_mini(self, app):
        """
        Test for valid registration with minimum possible fields.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.firstname, data.email = "", ""
        logging.info(f"email: {data.username}, pass: {data.password_1}, firstname: {data.password_2}")
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    def test_valid_register(self, app):
        """
        Test for valid registration with all possible fields.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    def test_register_username_already_exists(self, app):
        """
        Test for valid registration, username with special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = "111@111.ru"  # Юзернейм, который гарантированно есть в БД
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error_reg_page() == RegMessages.ALREADY_EXISTS

    @pytest.mark.parametrize("valid_special_ch", TestCases.VALID_SPECIAL_CHARACTERS)
    def test_invalid_username(self, app, valid_special_ch):
        """
        Test for username with valid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + valid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    @pytest.mark.parametrize("invalid_special_ch", TestCases.INVALID_SPECIAL_CHARACTERS)
    def test_invalid_username(self, app, invalid_special_ch):
        """
        Test for username with invalid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + invalid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error_reg_page() == RegMessages.USERNAME_WARNING

    def test_invalid_username_empty_field(self, app):
        """
        Test for username empty field.
        """
        pass

    def test_two_password_fields_did_not_match(self, app):
        """
        Test for invalid registration, two password fields did not match.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = "1"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error_reg_page() == RegMessages.TWO_PASS_DIDNT_MATCH

    def test_invalid_password1_empty_field(self, app):
        """
        Test for "Password" empty field.
        """
        pass

    def test_invalid_password2_empty_field(self, app):
        """
        Test for Password confirmation" empty field.
        """
        pass

    @pytest.mark.parametrize("short_password", TestCases.SHORT_PASSWORD)
    def test_short_password(self, app, short_password):
        """
        Test for short password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = short_password
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.SHORT_PASS in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}")

    @pytest.mark.parametrize("numeric_password", TestCases.NUMERIC_PASSWORD)
    def test_numeric_password(self, app, numeric_password):
        """
        Test for entirely numeric password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = numeric_password
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.ENTIRELY_NUMERIC_PASS in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, pass: {data.password_1}")

    @pytest.mark.parametrize("too_common_password", TestCases.TOO_COMMON_PASSWORD)
    def test_simple_password(self, app, too_common_password):
        """
        Test for entirely too common password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = too_common_password
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.TOO_COMMON_PASS in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, pass: {data.password_1}")

import pytest
import logging
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
        Test for valid registration, username with special characters
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = "111@111.ru"  # Юзерней, который гарантированно есть в БД
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_username_already_exists() == RegMessages.ALREADY_EXISTS

    @pytest.mark.parametrize("valid_special_ch", TestCases.VALID_SPECIAL_CHARACTERS)
    def test_invalid_email(self, app, valid_special_ch):
        """
        Test for username with valid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + valid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    @pytest.mark.parametrize("invalid_special_ch", TestCases.INVALID_SPECIAL_CHARACTERS)
    def test_invalid_email(self, app, invalid_special_ch):
        """
        Test for username with invalid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + invalid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_username_already_exists() == RegMessages.USERNAME_WARNING

    # def test_different_passwords(self, app):
    #     """
    #     Тест несовпадение паролей.
    #     """
    #     app.registration_page.open_registration_page()
    #     data = RegisterUserModel.random()
    #     data.password_2 = "drugoypass"
    #     app.registration_page.entry_data_registration(data=data)
    #     assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SECOND_PASS
    #
    # def test_short_passwords(self, app):
    #     """
    #     Тест на слишком короткий пароль.
    #     """
    #     app.registration_page.open_registration_page()
    #     data = RegisterUserModel.random()
    #     data.password_1 = "short"
    #     data.password_2 = "short"
    #     app.registration_page.entry_data_registration(data=data)
    #     assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_SHORT_PASS

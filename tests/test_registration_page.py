from fixtures.constants import RegMessages
from models.register import RegisterUserModel
# import pytest
# import time
# import json
# from selenium.webdriver.common.by import By
# from tests.constants_test_cases import TestCases


class TestRegistrationPage:
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
        Test for invalid registration, username already exists
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = "111@111.ru"  # Юзерней, который гарантированно есть в БД
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_username_already_exists() == RegMessages.ALREADY_EXISTS

    # @pytest.mark.parametrize("invalid_email", (TestCases.INVALID_EMAILS_LIST_FOR_REG))
    # def test_invalid_email(self, app, invalid_email):
    #     """
    #     Тесты на невалидный эмейл.
    #     """
    #     app.registration_page.open_registration_page()
    #     data = RegisterUserModel.random()
    #     data.email = invalid_email
    #     app.registration_page.entry_data_registration(data=data)
    #     assert app.registration_page.reg_status_big_red_tab() == RegMessages.INVALID_EMAIL[0]\
    #            + str(data.email[0]) + RegMessages.INVALID_EMAIL[1]

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

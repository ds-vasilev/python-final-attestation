import pytest
import logging
from fixtures.constants import RegMessages
from models.register import RegisterUserModel
from tests.constants_test_cases import DataCasesPasswords


class TestRegistrationPage:
    def test_valid_register_mini(self, app):
        """
        Test for valid registration with minimum possible fields.

        :notes: Test 1.
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

        :notes: Test 2.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    @pytest.mark.parametrize("error_text, variable, value",
                             DataCasesPasswords.INVALID_MESSAGES_CHECKER_ONE)
    def test_invalid_messages_one_param(self, app, error_text, variable, value):
        """
        Tests for invalid registration messages.

        :notes: Tests 3, 7, 14.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random_list()
        data[f"{variable}"] = value
        app.registration_page.entry_data_registration_form_control(data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert error_text in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, data: {data}")

    @pytest.mark.parametrize("valid_special_ch", DataCasesPasswords.VALID_SPECIAL_CHARACTERS)
    def test_invalid_username(self, app, valid_special_ch):
        """
        Test for username with valid special characters.

        :notes: Test 4.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + valid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN

    @pytest.mark.parametrize("invalid_special_ch", DataCasesPasswords.INVALID_SPECIAL_CHARACTERS)
    def test_invalid_username(self, app, invalid_special_ch):
        """
        Test for username with invalid special characters.

        :notes: Test 5.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + invalid_special_ch
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error_reg_page() == RegMessages.USERNAME_WARNING

    @pytest.mark.parametrize("variable, value", DataCasesPasswords.FORM_CONTROL_CHECK)
    def test_form_control(self, app, variable, value):
        """
        Tests for form-control.

        :notes: Tests 6, 8, 9, 15.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random_list()
        data[f"{variable}"] = value
        app.registration_page.entry_data_registration_form_control(data)
        logging.info(f"data: {data}")
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    @pytest.mark.parametrize("error_text, var1, val1, var2, val2",
                             DataCasesPasswords.INVALID_MESSAGES_CHECKER_TWO_PAR)
    def test_invalid_messages_two_param(self, app, error_text, var1, val1, var2, val2):
        """
        Tests for invalid registration messages with 2 param.

        :notes: Tests 10, 11, 12.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random_list()
        data[f"{var1}"] = val1
        data[f"{var2}"] = val2
        logging.info(f"data: {data}")
        app.registration_page.entry_data_registration_form_control(data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        logging.info(f"errors: {all_errors_msgs}")
        assert error_text in all_errors_msgs

    def test_pass_and_username_similar(self, app):
        """
        Test for similar pass and username.

        :notes: Test 13.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = data.username
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.PASS_SIMILAR_TO_THE_USERNAME in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, pass: {data.email}")

    @pytest.mark.parametrize("age", DataCasesPasswords.AGE_CONTROL_FORM_CONTROL)
    def test_invalid_age(self, app, age):
        """
        Test for invalid age with form-control.

        :notes: :Test 16.
        """
        app.registration_page.open_registration_page()
        app.registration_page.clear_and_fill(age)
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    @pytest.mark.parametrize("age", DataCasesPasswords.AGE_CONTROL)
    def test_invalid_age(self, app, age):
        """
        Test for invalid age.

        :notes: Tests 17.
        """
        app.registration_page.open_registration_page()
        app.registration_page.clear_and_fill(age)
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.SO_YOUNG in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}")

    @pytest.mark.xfail
    def test_valid_avatar_upload(self, app):
        """
        Test for valid avatar upload.

        :notes: Tests 18.
        """
        app.registration_page.open_registration_page()
        img = "C:/GitHub/python-final-attestation/.github/images/vaild_ava.jpg"
        # img = f"https://raw.githubusercontent.com/ds-vasilev/python-final-attestation/master/" \
        #       f".github/images/vaild_ava.jpg"
        # img = Path("python-final-attestation", "tests", "vaild_ava.jpg")
        # img = "./vaild_ava.jpg"
        app.registration_page.avatar_upload(file_path=img)
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN
        app.registration_page.login(username=data.username, password=data.password_1)
        app.registration_page.enter_on_profile_page()
        assert "Currently" in app.registration_page.profile_image_check()

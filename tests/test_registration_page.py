import pytest
import logging
from fixtures.constants import RegMessages
from models.register import RegisterUserModel
from tests.constants_test_cases import DataCasesPasswords


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

    @pytest.mark.parametrize("valid_special_ch", DataCasesPasswords.VALID_SPECIAL_CHARACTERS)
    def test_invalid_username(self, app, valid_special_ch):
        """
        Test for username with valid special characters.
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
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = 0
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

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
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = 0
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    def test_invalid_password2_empty_field(self, app):
        """
        Test for Password confirmation empty field.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = 0
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    @pytest.mark.parametrize("short_password", DataCasesPasswords.SHORT_PASSWORD)
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

    @pytest.mark.parametrize("numeric_password", DataCasesPasswords.NUMERIC_PASSWORD)
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

    @pytest.mark.parametrize("too_common_password", DataCasesPasswords.TOO_COMMON_PASSWORD)
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

    @pytest.mark.parametrize("form_control_password", DataCasesPasswords.FORM_CONTROL_PASSWORD)
    def test_simple_password(self, app, form_control_password):
        """
        Test for entirely passwords form-control.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = form_control_password
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    def test_pass_and_username_similar(self, app):
        """
        Test for similar pass and username.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = data.username
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.PASS_SIMILAR_TO_THE_USERNAME in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, pass: {data.email}")

    @pytest.mark.parametrize("invalid_email", DataCasesPasswords.INVALID_EMAILS_LIST_FOR_REG)
    def test_invalid_email(self, app, invalid_email):
        """
        Test for invalid email.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = invalid_email
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.INVALID_EMAIL in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}, pass: {data.email}")

    @pytest.mark.parametrize("age", DataCasesPasswords.AGE_CONTROL)
    def test_invalid_age(self, app, age):
        """
        Test for invalid age.
        """
        app.registration_page.open_registration_page()
        app.registration_page.clear_and_fill(age)
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        all_errors_msgs = app.registration_page.text_many_errors_reg_page()
        assert RegMessages.SO_YOUNG in all_errors_msgs
        logging.info(f"errors: {all_errors_msgs}")

    @pytest.mark.parametrize("age", DataCasesPasswords.AGE_CONTROL_FORM_CONTROL)
    def test_invalid_age(self, app, age):
        """
        Test for invalid age with form-control.
        """
        app.registration_page.open_registration_page()
        app.registration_page.clear_and_fill(age)
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_on_head_in_registration_page() == RegMessages.REGISTER

    # def test_valid_avatar_upload(self, app):
    #     """
    #     Test for valid avatar upload.
    #     """
    #     app.registration_page.open_registration_page()
    #     img = "C:/GitHub/python-final-attestation/.github/images/vaild_ava.jpg"
    #     img = f"https://raw.githubusercontent.com/ds-vasilev/python-final-attestation/master/" \
    #           f".github/images/vaild_ava.jpg"
    #     # img = Path("python-final-attestation", "tests", "vaild_ava.jpg")
    #     # img = "./vaild_ava.jpg"
    #
    #     app.registration_page.avatar_upload(file_path=img)
    #     data = RegisterUserModel.random()
    #     app.registration_page.entry_data_registration(data=data)
    #     assert app.registration_page.text_on_head_in_log_in_page() == RegMessages.LOG_IN
    #     app.registration_page.login(username=data.username, password=data.password_1)
    #     app.registration_page.enter_on_profile_page()
    #     assert "Currently" in app.registration_page.profile_image_check()

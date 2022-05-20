from faker import Faker
import logging
fake = Faker()


class RegisterUserModel:
    """
    User generator.
    """
    def __init__(self, username: str = None, password_1: str = None,
                 password_2: str = None, firstname: str = None, email: str = None):
        self.username = username
        self.firstname = firstname
        self.password_1 = password_1
        self.password_2 = password_2
        self.email = email

    @staticmethod
    def random():
        firstname = fake.first_name()
        username_ = firstname + fake.last_name()
        email_ = fake.email()
        password = fake.password()
        logging.info(f"user: {username_}, email: {email_}, pass: {password}, firstname: {firstname}")
        return RegisterUserModel(email=email_, password_1=password,
                                 password_2=password, firstname=firstname, username=username_)

    @staticmethod
    def random_list() -> dict:
        """
        Dict realisation for parametrization.
        """
        first_name = fake.first_name()
        password = fake.password()
        new_user = dict(
            firstname = first_name,
            username = first_name + fake.last_name(),
            email = fake.email(),
            password_1 = password,
            password_2 = password
        )
        return new_user

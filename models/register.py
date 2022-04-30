from faker import Faker
import logging

fake = Faker()


class RegisterUserModel:
    """
    User generator.
    """
    def __init__(self, email: str = None, password_1: str = None,
                 password_2: str = None, firstname: str = None):
        self.username = email
        self.firstname = firstname
        self.password_1 = password_1
        self.password_2 = password_2
        self.email = email

    @staticmethod
    def random():
        email_ = fake.email()
        password = fake.password()
        firstname = fake.first_name()
        logging.info(f"email: {email_}, pass: {password}, firstname: {firstname}")
        return RegisterUserModel(email=email_, password_1=password,
                                 password_2=password, firstname=firstname)

class RegMessages:
    LOG_IN = "Log in"
    REGISTER = "Register new user"
    ALREADY_EXISTS = "A user with that username already exists."
    USERNAME_WARNING = "Enter a valid username. This value may contain " \
                       "only letters, numbers, and @/./+/-/_ characters."
    TWO_PASS_DIDNT_MATCH = "The two password fields didn’t match."
    SHORT_PASS = "This password is too short. It must contain at least 8 characters."
    TOO_COMMON_PASS = "This password is too common."
    ENTIRELY_NUMERIC_PASS = "This password is entirely numeric."
    INVALID_EMAIL = "Enter a valid email address."
    PASS_SIMILAR_TO_THE_USERNAME = "The password is too similar to the username."
    SO_YOUNG = "You are young!"

class LogMessages:
    LOG_IN = "Log in"
    ERROR_USERNAME_OR_PASS = f"Please enter a correct username and password. " \
                             f"Note that both fields may be case-sensitive."
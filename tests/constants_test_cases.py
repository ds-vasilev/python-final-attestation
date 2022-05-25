class DataCasesPasswords:
    VALID_SPECIAL_CHARACTERS = [
        "@",
        ".",
        "+",
        "-",
        "_",
    ]

    INVALID_SPECIAL_CHARACTERS = [
        "!",
        "#",
    ]

    AGE_CONTROL = [
        "0",
        "1",
        "17",
    ]

    AGE_CONTROL_FORM_CONTROL = [
        "-1",
        "18.5",
        "ывыы",
    ]

    INVALID_EMPTY_DATA_FOR_LOG_PAGE = [
        ["", "testtesttest"],
        ["test", ""],
    ]

    INVALID_DATA_FOR_LOG_PAGE = [
        ["@", "1111111111111"],
        ["test", "Iloveyou"],
    ]

    FORM_CONTROL_CHECK = [
        ["username", ""],
        ["password_1", ""],
        ["password_2", ""],
        ["email", "nekorrektnii.email"],
        ["email", "@nekorrektniiemail.com"],
    ]

    INVALID_MESSAGES_CHECKER_ONE = [
        ["A user with that username already exists.", "username", "111@111.ru"],
        ["The two password fields didn’t match.", "password_2", "1"],
        ["Enter a valid email address.", "email", "nekorrektnii@email"],
        ["Enter a valid email address.", "email", "nekorrektnii@ru"],
        ["Enter a valid email address.", "email", "nekorre.ktnii@mail"],
    ]

    INVALID_MESSAGES_CHECKER_TWO_PAR = [
        ["This password is too short. It must contain at least 8 characters.",
         "password_1", "1", "password_2", "1"],
        ["This password is too short. It must contain at least 8 characters.",
         "password_1", "1@a1Q$s", "password_2", "1@a1Q$s"],
        ["This password is too short. It must contain at least 8 characters.",
         "password_1", "1@a1Q$s", "password_2", "1@a1Q$s"],
        ["This password is entirely numeric.",
         "password_1", "0", "password_2", "0"],
        ["This password is entirely numeric.",
         "password_1", "1", "password_2", "1"],
        ["This password is entirely numeric.",
         "password_1", "12345678", "password_2", "12345678"],
        ["This password is too common.",
         "password_1", "Iloveyou", "password_2", "Iloveyou"],
    ]

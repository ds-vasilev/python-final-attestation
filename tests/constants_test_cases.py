from random import randint


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
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        "/",
        "`",
    ]

    SHORT_PASSWORD = [
        "1",
        "1@a1Q$s",
    ]

    NUMERIC_PASSWORD = [
        "0",
        randint(1, 999999),
        randint(12345678, 123456789),
    ]

    TOO_COMMON_PASSWORD = [
        "Iloveyou",
    ]

    FORM_CONTROL_PASSWORD = [
        ["nekorrektnii.email"],
        ["@nekorrektniiemail.com"],
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

    INVALID_EMAILS_LIST_FOR_REG = [
        ["nekorrektnii@email"],
        ["nekorrektnii@ru"],
        ["nekorre.ktnii@mail"],
    ]

    INVALID_EMPTY_DATA_FOR_LOG_PAGE = [
        ["", "testtesttest"],
        ["test", ""],
    ]

    INVALID_DATA_FOR_LOG_PAGE = [
        ["@", "1111111111111"],
        ["test", "Iloveyou"],
    ]

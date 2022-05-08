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
        randint(1,999999),
        randint(12345678,123456789),
    ]

    TOO_COMMON_PASSWORD = [
        "Iloveyou",
    ]

    AGE_CONTROL = [
        "0",
        "1",
        "17",
    ]

    INVALID_EMAILS_LIST_FOR_REG = [
        ["nekorrektnii@email"],
        ["nekorrektnii@ru"],
        ["nekorre.ktnii@mail"],
    ]

    INVALID_DATA_FOR_LOG_PAGE = [
        ["", ""],
        ["invalid", "invalid"],
        ["111@test.ru", ""],
        ["", "11111111"],
    ]

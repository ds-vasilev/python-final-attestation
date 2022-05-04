from random import randint


class TestCases:
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
        "1@",
        "1@a",
        "1@a1",
        "1@a1Q",
        "1@a1Q$",
        "1@a1Q$s",
    ]

    NUMERIC_PASSWORD = [
        "0",
        randint(1,999999),
        randint(12345678,123456789),
    ]

    TOO_COMMON_PASSWORD = [
        "123qweasd",
        "aaaaaaaaaa",
        "Password",
        "Admin123",
        "Iloveyou",
        "Qwertyuiop",
        "Qwerty123",
        "Qwertyuiop",
        "1234567890",
        "123456",
        "password",
        "12345678",
        "qwerty",
        "123456789",
        "12345",
        "1234",
        "111111",
        "1234567",
        "dragon",
        "123123",
        "baseball",
        "abc123",
        "football",
        "monkey",
        "letmein",
        "696969",
    ]

    INVALID_EMAILS_LIST_FOR_REG = [
        ["nekorrektnii#email"],
        ["nekorrektnii@email"],
        ["nekorrektnii.ru"],
        ["nekorrektnii@.ru"],
        ["@nekorrektnii.ru"],
        ["nekorrektnii@ru"],
        ["nekorre.ktnii@mail"],
        ["@nekorrektnii.mail"],
        ["биба@яндекс.рф"],  # сайт не работает с кирилическими доменами
    ]

    INVALID_DATA_FOR_LOG_PAGE = [
        ["", ""],
        ["invalid", "invalid"],
        ["111@test.ru", ""],
        ["", "11111111"],
    ]

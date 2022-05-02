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

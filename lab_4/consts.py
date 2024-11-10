conversion_factors_mass = {
    "граммы": 1,
    "килограммы": 1000,
    "фунты": 453.592,
    "унции": 28.3495,
}


conversion_functions_temperature = {
    "Цельсий": {
        "Фаренгейт": lambda x: (x * 9 / 5) + 32,
        "Кельвин": lambda x: x + 273.15,
        "Цельсий": lambda x: x,
    },
    "Фаренгейт": {
        "Цельсий": lambda x: (x - 32) * 5 / 9,
        "Кельвин": lambda x: (x - 32) * 5 / 9 + 273.15,
        "Фаренгейт": lambda x: x,
    },
    "Кельвин": {
        "Цельсий": lambda x: x - 273.15,
        "Фаренгейт": lambda x: (x - 273.15) * 9 / 5 + 32,
        "Кельвин": lambda x: x,
    },
}


conversion_factors_length = {
    "метры": 1,
    "километры": 1000,
    "мили": 1609.34,
    "футы": 0.3048,
}

log_file = "converter.log"
